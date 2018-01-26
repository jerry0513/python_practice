#--------------------------------
# 匯入外部模組
#--------------------------------
import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

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

X = data[:, features]
y = data[:, label]
estimator = SVR(kernel="linear")
selector = RFE(estimator, 5, step=1)
selector = selector.fit(X, y)

print(selector.support_)
print(selector.ranking_)