from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot(
    "Chat Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="database.db",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.SpecificResponseAdapter"
    ],
    read_only=True
)

trainer = ChatterBotCorpusTrainer(bot)

unsureResponse = "My ChatBot is unsure of this question or conversation, please to improve this ChatBot input the " \
                 "expect response to the question u previously ask "

takingNote = "I'm taking note of this"

for filename in os.listdir(r"C:\Users\Louis\Documents\gitKraken\ChatBot\finalProject\ChatBot\categories"):
    trainer.train("ChatBot/categories/" + filename)

trainer.train("chatterbot.corpus.english")


def chatbot(message,):
    bot_input = bot.get_response(message)
    if bot_input.confidence >= 0.6:
        return bot_input.serialize()
    else:
        return unsureResponse


def learningResponse(msg, last_message):
    bot.learn_response(msg, last_message)
    return takingNote