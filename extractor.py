import re
import sqlite3
from typing import IO, Literal


def map_rows(results: list) -> list:
    """Maps one-column rows to a flat list"""
    return list(map(lambda row: row[0], results))


def discard(message: str):
    """Filters automatic or deleted messages."""
    if re.match('^<?(media omitted|GIF omitted)>?$', message, flags=re.RegexFlag.IGNORECASE):
        return True
    if re.match('^\[\d{2}\/\d{2}, \d{2}\:\d{2}\] (.+?): ', message):
        return True


class WhatsappExtractor:
    REGEX = {
        "android": {
            "capture_stamp": '^.+? -'
        },
        "ios": {
            "capture_stamp": '^\\[\\d{2}\\/\\d{2}\/\\d{2} \\d{2}\\:\\d{2}:\\d{2}\\]'
        }
    }

    def __init__(self, platform: Literal['android', 'ios']):
        self.platform = platform
        self.database = sqlite3.connect('training_data/chats.db')
        self.database.execute('CREATE TABLE IF NOT EXISTS conversations (message text NOT NULL, contact text NOT NULL)')

    def get_regex(self, key: str) -> str:
        """Returns the regex subpattern for the current platform"""
        return self.REGEX[self.platform][key]

    def extract(self, dump_file: IO):
        """Extract all messages from an exported Whatsapp conversation"""
        last_id = 0
        for line in dump_file:
            line = re.sub('([‎⁨⁩]|\n$)', '', line)
            matches = re.search(f'{self.get_regex("capture_stamp")} (.+?): (.+)$', line)
            if matches:
                contact = matches.group(1)
                message = matches.group(2)
                if discard(message):
                    continue
                cursor = self.database.execute('INSERT INTO conversations (contact, message) VALUES (?,?)',
                                               (contact, message))
                last_id = cursor.lastrowid
            else:
                self.database.execute("UPDATE conversations SET message=(message || '\n' || ?) WHERE rowid == ?",
                                      (line, last_id))
        self.database.commit()

    def contacts(self):
        """Returns a list of all contacts in this conversation."""
        query = self.database.execute('SELECT contact FROM conversations GROUP BY contact')
        results = query.fetchall()
        return map_rows(results)

    def messages_from(self, contact: str):
        """Returns a list of messages from :contact:"""
        query = self.database.execute('SELECT message FROM conversations WHERE contact == ?', (contact,))
        results = query.fetchall()
        return map_rows(results)
