from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn import metrics


def find_accuracy(model, x, y, x_test, y_test):
    model.fit(x, y)
    y_pred = model.predict(x_test)
    return metrics.accuracy_score(y_test, y_pred)

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

knn1 = KNeighborsClassifier(n_neighbors=1)
print find_accuracy(knn1, X_train, y_train, X_test, y_test)

knn5 = KNeighborsClassifier(n_neighbors=5)
print find_accuracy(knn5, X_train, y_train, X_test, y_test)

logR = LogisticRegression()
print find_accuracy(logR, X_train, y_train, X_test, y_test)