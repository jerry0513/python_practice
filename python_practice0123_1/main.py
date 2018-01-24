import jieba
data = []
with open('data.txt', 'r', encoding='UTF-8') as textData:
    d = textData.read()
    data = list(jieba.cut(d))

positives = []
with open('positives.txt', 'r', encoding='UTF-8') as positivesData:
    for d in positivesData.readlines():
        d = d.strip()
        positives.append(d)

    positivesWord = []
    for k in data:
        if k in positives:
            positivesWord.append(k)
    print(positivesWord)
    print(len(positivesWord))

negatives = []
with open('negatives.txt', 'r', encoding='UTF-8') as negativesData:
    for d in negativesData.readlines():
        d = d.strip()
        negatives.append(d)

    negativesWord = []
    for k in data:
        if k in negatives:
            negativesWord.append(k)
    print(negativesWord)
    print(len(negativesWord))