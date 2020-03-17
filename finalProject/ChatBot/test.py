from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot(
    "Chat Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="database.db"
)

trainer = ChatterBotCorpusTrainer(bot)

for filename in os.listdir(r"C:\Users\Louis\Documents\gitKraken\ChatBot\finalProject\ChatBot\categories"):
        trainer.train("categories/"+filename)

print("type something")

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt):
        break
