import myLexi

with open('testSentences.csv', 'r', encoding='UTF-8') as file:
    right = 0
    wrong = 0
    for data in file.readlines():
        items = data.split(',')
        result, ps, ng = myLexi.senti(items[1])  # 接收回傳的三個值

        senti = float(items[3]) - 5
        k = 0
        if result == 'Positive!':
            k=1
        else:
            k=-1

        if senti*k > 0:
            right = right + 1
        else:
            wrong = wrong + 1

        print(ps)
        print(ng)
        print(result)
    print(right)
    print(wrong)