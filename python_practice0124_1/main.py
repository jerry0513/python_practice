import myLexi

with open('data.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    result, ps, ng = myLexi.senti(data)  # 接收回傳的三個值
    print(result)
    print(ps)
    print(ng)