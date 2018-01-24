import jieba

def senti(doc):
    sentiWords = {}
    sentiSegs = []
    sentiVal = []

    with open('sentimentWords.csv', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            items = data.split(',')
            sentiWords[items[1]] = items[2]

    s = jieba.cut(doc)
    for k in s:
        try:
            sentiVal.append(sentiWords[k])
            sentiSegs.append(k)
        except:
            pass

    ev = 0
    for k in sentiVal:
        ev = ev + (float(k) - 5)

    return sentiSegs, sentiVal, ev/len(sentiVal)