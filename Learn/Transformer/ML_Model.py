#https://www.apriorit.com/dev-blog/768-ai-develop-smart-chatbots-using-python#cre
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
FlightBot= ChatBot(
    name = 'MathsBot',
    read_only = False,                  
    logic_adapters = [
        'chatterbot.logic.BestMatch'

    ],                 
    storage_adapter = "chatterbot.storage.SQLStorageAdapter"
)
corpus_trainer = ChatterBotCorpusTrainer(FlightBot)
corpus_trainer.train("chatterbot.corpus.english")

conv_1 = [
    "Hey! I need some help!",
    "Hi, how can I help you?",
    "I'd like to book a flight to Iceland.",
    "Your flight has been booked."
]

# ....

# conv_n = [
#     "....",
#     ......
# ]

list_trainer = ListTrainer(FlightBot)

list_trainer.train(conv_1)
# ....
# list_trainer.train(conv_n) # where n - number of conversations

while True:
    query = input()
    if query=='stop':
        break
    bot_input = FlightBot.get_response(query)
    print(bot_input)