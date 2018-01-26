#--------------------------------
# 匯入外部模組
#--------------------------------
import numpy as np
from sklearn import svm
from sklearn.naive_bayes import GaussianNB, BernoulliNB

#-------------------------------------------------
# 讀取資料
#-------------------------------------------------
data=np.genfromtxt('data.csv', delimiter=',')

#---------------------------
# 亂數重排資料
#---------------------------
np.random.shuffle(data)

#***************************
# 參數設定
#***************************
tn=120
features=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
label=0

#---------------------------
# 訓練資料及標籤
#---------------------------
training_data  = data[:tn, features]
training_label = data[:tn, label]

#---------------------------
# 測試資料及標籤
#---------------------------
testing_data  = data[tn:, features]
testing_label = data[tn:, label]


#***********************************************
# 建立自動分類機器人
#***********************************************
# svm_rbf = svm.SVC(kernel='rbf')
# svm_rbf.fit(training_data, training_label)
# nb = GaussianNB()
nb = BernoulliNB()

nb.fit(training_data, training_label)

#---------------------------
# 分類機器人測試
#---------------------------
print('正確:', testing_label)
print('-'*60)

# predict = svm_rbf.predict(testing_data)
predict = nb.predict(testing_data)

print('預測:', predict)
print('-'*60)

#---------------------------
# 和正確資料比對
#---------------------------
results = testing_label == predict
print('比對:', results)
print('-'*60)

#---------------------------
# 正確率
#---------------------------
print('正確率:', round(np.sum(results)/len(results), 2))
print('-'*60)