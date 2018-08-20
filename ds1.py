import numpy as np

from sklearn import tree

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

height = np.random.randint(low=140, high=195)
weight = np.random.randint(low=45, high=100)
size = np.random.randint(low=37, high=48)

test = [[height, weight, size]]

treeClf = tree.DecisionTreeClassifier()

treeClf = treeClf.fit(X,Y)

predictionTree = treeClf.predict(test)

neighClf = KNeighborsClassifier()

neighClf = neighClf.fit(X,Y)

predictionNeigh = neighClf.predict(test)

svcClf = SVC()

svcClf = svcClf.fit(X,Y)

predictionSvc = svcClf.predict(test)

print(test)
print("Decision Tree: ", predictionTree)
print("Neighbour: ", predictionNeigh)
print("SVC: ", predictionSvc)
