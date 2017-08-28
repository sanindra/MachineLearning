from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#train set is test set
def find_accuracy(model, x, y):
    model.fit(x, y)
    y_pred = model.predict(x)
    return metrics.accuracy_score(y, y_pred)

iris = load_iris()
x = iris.data
y = iris.target
knn1 = KNeighborsClassifier(n_neighbors=1)
print find_accuracy(knn1, x, y)

knn5 = KNeighborsClassifier(n_neighbors=5)
print find_accuracy(knn5, x, y)

logR = LogisticRegression()
print find_accuracy(logR, x, y)