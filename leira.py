# -*- coding: utf-8 -*-
"""Dumb chatbot trained on WhatsApp conversations"""
import logging
from chatterbot import ChatBot

from trainer import trainbot

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
            'threshold': 0.25,
            'default_response': 'wat tendi nada'
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ]
)
trainbot(LEIRA)

print("Bot operational, type away!")
while True:
    try:
        bot_input = LEIRA.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
print("Goodbye human o.o")
