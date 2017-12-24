# -*- coding: utf-8 -*-
"""Training functions for the bot"""
from chatparser import readchats
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


def trainbot(bot):
    """Trains the chatbot"""

    def trainwhatsapp(conversations):
        """Uses WhatsApp chats in the training_data folder to train the bot"""
        bot.set_trainer(ListTrainer)
        for chat in conversations:
            bot.train(chat)

    def traincorpus():
        """Uses the included Chatterbot corpus to train the bot"""
        bot.set_trainer(ChatterBotCorpusTrainer)
        bot.train(
            "chatterbot.corpus.english",
            "chatterbot.corpus.portuguese"
        )

    traincorpus()
    trainwhatsapp(readchats())
