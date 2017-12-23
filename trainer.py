# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


def trainMyBot(bot):
    """"""
    def trainWhatsApp(conversations):
        bot.set_trainer(ListTrainer)
        for statement in conversations:

    def trainCorpus():
        bot.set_trainer(ChatterBotCorpusTrainer)
        bot.train(
            "chatterbot.corpus.english",
            "chatterbot.corpus.portuguese"
        )
