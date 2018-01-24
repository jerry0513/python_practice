import jieba
jieba.load_userdict('user.txt')
seg_list = jieba.cut("我來到國立臺北商業大學", cut_all=False)
seg_list2 = jieba.cut("我來自國立臺北商業大學資訊管理系", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))
print("Full Mode: " + "/ ".join(seg_list2))