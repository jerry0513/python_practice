import jieba

posWords = set()
negWords = set()

def senti(doc):
    global posWords
    global negWords
    posSegs = []
    negSegs = []

    if len(posWords) == 0:
        with open('positives.txt', 'r', encoding='UTF-8') as file:
            for data in file.readlines():
                data = data.strip()
                posWords.add(data)

    if len(negWords) == 0:
        with open('negatives.txt', 'r', encoding='UTF-8') as file:
            for data in file.readlines():
                data = data.strip()
                negWords.add(data)

    cutData = jieba.cut(doc)
    for c in cutData:
        if c in posWords:
            posSegs.append(c)
        if c in negWords:
            negSegs.append(c)

    if len(posSegs) > len(negSegs):
        return 'Positive!', posSegs, negSegs
    else:
        return 'Negative!', posSegs, negSegs