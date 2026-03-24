from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
PolarBot= ChatBot(
        name = 'MathsBot',
        read_only = False,                  
        logic_adapters = [
            'chatterbot.logic.BestMatch'

        ],                 
        storage_adapter = "chatterbot.storage.SQLStorageAdapter"
    )
matched_words = ['plea', 'bargain', 'innocent', 'prosecutor', 'system', 'defendant', 'justice', 'lawyer', 'judge']
trainInputData = []
trainTargetData = []
with open("targetText.txt", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    for line in lines:
        line = line.split("$$$")
        trainInputData.append(line[0])
        trainTargetData.append(line[2])

def subject(user_phrase):
    #subject is the bias and phrase
    subject = [user_phrase[0],user_phrase[1]]
    for word in matched_words:
        if word in user_phrase: 
            subject.append(word)
    return subject

def generator(code):
    return response

def train():
    corpus_trainer = ChatterBotCorpusTrainer(PolarBot)
    #corpus_trainer.train("chatterbot.corpus.english")
    list_trainer = ListTrainer(PolarBot)
    for trainInput, trainTarget in zip(trainInputData, trainTargetData):
        print(type(trainInput),type(trainTarget) ) 
        conversation = [
        trainInput, 
        trainTarget
        ]
        list_trainer.train(conversation)


    # ....

    # conv_n = [
    #     "....",
    #     ......
    # ]

    list_trainer = ListTrainer(PolarBot)

    list_trainer.train(conversation)
    # ....
    # list_trainer.train(conv_n) # where n - number of conversations

    while True:
        query = input()
        if query=='stop':
            break
        bot_input = PolarBot.get_response(query)
        print(bot_input)
def test():
    while True:
        query = input()
        if query=='stop':
            break
        bot_input = PolarBot.get_response(query)
        print(bot_input)
train()