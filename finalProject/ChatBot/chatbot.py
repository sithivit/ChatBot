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
        "chatterbot.logic.SpecificResponseAdapter",
        "chatterbot.logic.TimeLogicAdapter"
    ]
)

trainer = ChatterBotCorpusTrainer(bot)

for filename in os.listdir(r"C:\Users\Louis\Documents\gitKraken\ChatBot\finalProject\ChatBot\categories"):
    trainer.train("ChatBot/categories/" + filename)


def chatbot(message):
    bot_input = bot.get_response(message)
    return bot_input.serialize()
