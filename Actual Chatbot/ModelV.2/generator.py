matched_words = ['plea', 'bargain', 'innocent', 'prosecutor', 'system', 'defendant', 'justice', 'lawyer', 'judge']
trainInputData = []
responses = []
with open("targetText.txt", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    for line in lines:
        line = line.split("$$$")
        trainInputPoint = line[0]
        trainInputData.append(trainInputPoint.lower())
with open('sampleGeneration.txt', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    for line in lines:
        responses.append(line)

def subject(user_phrase):
    #subject is the bias and phrase
    subject = [user_phrase[0],user_phrase[1]]
    for word in matched_words:
        if word in user_phrase: 
            subject.append(word)
    return subject

def generator(code):
    code = int(code)
    response = responses[code]
    return response