import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data=np.genfromtxt('winequality-white.csv',  delimiter=';')
np.random.shuffle(data)

n = 3500
features = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
label = 11
training = data[:n]
testing = data[n:]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(training[:, features], training[:, label])

predicted = knn.predict(testing[:, features])
print (predicted)

excepted = testing[:, label]
print(excepted)

result = (predicted == excepted)
print(result)

count = np.sum(result)
print(count/len(testing))