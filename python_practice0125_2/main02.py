import numpy as np
from sklearn.svm import SVC

data=np.genfromtxt('web_phishing.csv',  delimiter=',')
np.random.shuffle(data)

n = 900
features = [0, 1, 2, 3, 4, 5, 6, 7, 8]
label = 9
training = data[:n]
testing = data[n:]

svm = SVC(kernel='rbf')
svm.fit(training[:, features], training[:, label])

predicted = svm.predict(testing[:, features])
print (predicted)

excepted = testing[:, label]
print(excepted)

result = (predicted == excepted)
print(result)

count = np.sum(result)
print(count/len(testing))