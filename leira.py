# -*- coding: utf-8 -*-
"""
"""
from chatterbot import ChatBot

import logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'Leira',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database='',
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
