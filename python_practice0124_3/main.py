import myLexi

with open('data.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    sentiSegs, sentiVal, ev= myLexi.senti(data)  # 接收回傳的三個值
    print(sentiSegs)
    print(sentiVal)
    print(ev)