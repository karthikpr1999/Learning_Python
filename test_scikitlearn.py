from sklearn import svm
from sklearn import datasets,cluster
from sklearn import linear_model
from sklearn import neighbors
# Load dataset
iris = datasets.load_iris()
clf = svm.LinearSVC()
# learn from the data
clf.fit(iris.data, iris.target)
# predict for unseen data
clf.predict([[ 5.0,  3.6,  1.3,  0.25]])
# Parameters of model can be changed by using the attributes ending with an underscore
print(clf.coef_ )
reg = linear_model.LinearRegression()
# use it to fit a data
reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# Let's look into the fitted data
print(reg.coef_)
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target)
# Predict and print the result
result=knn.predict([[0.1, 0.2, 0.3, 0.4]])
print(result)
# create clusters for k=3
k=3
k_means = cluster.KMeans(k)
# fit data
k_means.fit(iris.data)
# print results
print( k_means.labels_[::10])
print( iris.target[::10])