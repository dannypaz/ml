from sklearn import tree

SMOOTH = 1
BUMPY = 0

features = [
    [140, SMOOTH],
    [130, SMOOTH],
    [150, BUMPY],
    [170, BUMPY]
]

APPLE = 0
ORANGE = 1

labels = [APPLE, APPLE, ORANGE, ORANGE]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# output is 0 if apple and 1 if orange
print(clf.predict([[160, 0]]))
