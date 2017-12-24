"""
    Contains all leirabot exceptions
"""


class BotError(Exception):
    """Base class for all leirabot runtime exceptions"""

    def __init__(self, bot=None, msg=None):
        if bot is None:
            botname = "Uninitialized"
            self.bot = None
        else:
            self.bot = bot
            botname = bot.name
        if msg is None:
            msg = "An unspecified error occured with bot %s" % botname
        super(BotError, self).__init__(msg)


class ParseError(BotError):
    """Error when parsing WhatsApp .txt files"""

    def __init__(self, bot, fname, line):
        super(ParseError, self).__init__(
            msg="Error parsing file %s at line %d" % (fname, line)
        )
        self.filename = fname
        self.line = line
