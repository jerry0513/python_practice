#--------------------------------
# 匯入外部模組
#--------------------------------
import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


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
features=[1, 7, 8, 11, 12]
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


#---------------------------
# 找較好的C及gamma值
#---------------------------
# param_grid = {'C': [0.1, 0.5, 1, 5, 10, 15, 20, 100, 150, 175, 200, 250, 1000],
#               'gamma': [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2, 3, 4, 5, 10], } #範圍縮小更精準
param_grid = {'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'gamma': [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007], }
clf = GridSearchCV(svm.SVC(kernel='rbf'), param_grid)
clf.fit(training_data, training_label)

print("找出較好的C及gamma")
best_C=clf.best_estimator_.C
best_gamma=clf.best_estimator_.gamma

print('C =', best_C)
print('gamma =', best_gamma)
print('-'*60)


#***********************************************
# 建立自動分類機器人
#***********************************************
svm_rbf = svm.SVC(kernel='rbf', gamma=best_gamma, C=best_C)
svm_rbf.fit(training_data, training_label)

print('分類機器人參數')
print(svm_rbf)
print('-'*60)

#---------------------------
# 分類機器人測試
#---------------------------
print('正確:', testing_label)
print('-'*60)

predict = svm_rbf.predict(testing_data)
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

pca = PCA(n_components=2)

X = data[:, features]
y = data[:, label]

pca.fit(X)
print(pca.explained_variance_ratio_)

new_data = pca.transform(X)



#---------------------------
# 圖形設定
#---------------------------
fig = plt.figure()
sub = fig.add_subplot(111)

#---------------------------
# 資料分割群
#---------------------------
data1 = new_data[y==1]
data2 = new_data[y==2]
data3 = new_data[y==3]

#---------------------------
# 繪製資料
#---------------------------
sub.plot(data1[:, 0], data1[:,1], 'bd', alpha=0.2)
sub.plot(data2[:, 0], data2[:,1], 'ro', alpha=0.2)
sub.plot(data3[:, 0], data3[:,1], 'g^', alpha=0.2)


#---------------------------
# 設定圖標題
#---------------------------
plt.title('Iris flower')

#---------------------------
# 設定資料說明
#---------------------------
plt.legend(['setosa', 'versicolor', 'virginica'], numpoints=1, loc='upper left')

#---------------------------
# 設定格線
#---------------------------
plt.grid(True)

#---------------------------
# 顯示圖形
#---------------------------
plt.show()
