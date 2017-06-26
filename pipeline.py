from sklearn import datasets
iris = datasets.load_iris()

# f(x) = y
#
X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
# test_size .5 is just saying 'I want half the data in each'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

from sklearn import tree #, neighbors

# Use the tree
clf = tree.DecisionTreeClassifier()
# Use Knn
# clf = neighbors.KNeighborsClassifier()

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
