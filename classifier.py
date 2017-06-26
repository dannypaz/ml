from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from danlearn.scrappy import ScrappyKNN

# Data start
iris = datasets.load_iris()

# Seperate into axis
X = iris.data
y = iris.target

# Split the data for our classifier
# test_size .5 is just saying 'I want half the data in each'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# Write the classifier
clf = ScrappyKNN()

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

print(accuracy_score(y_test, predictions))
