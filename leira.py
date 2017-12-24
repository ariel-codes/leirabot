# -*- coding: utf-8 -*-
"""Dumb chatbot trained on WhatsApp conversations"""
import logging
import os
import time

from chatterbot import ChatBot, utils

from trainer import trainbot


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# logging.basicConfig(level=logging.INFO)


LEIRA = ChatBot(
    'Leira',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database='chatbot',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.50,
            'default_response': 'wat tendi nada'
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ]
)
trainbot(LEIRA)

clear()
print("Bot operational, type away!")
time.sleep(2)

while True:
    try:
        bot_input = LEIRA.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

clear()
print("Goodbye human o.o")
time.sleep(2)
