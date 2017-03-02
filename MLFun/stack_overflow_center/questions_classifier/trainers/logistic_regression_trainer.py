
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression


def train(features, labels):
    best_score = 0
    result = None

    cross_validation = KFold(n=len(features), n_folds=5)

    for (train, test) in cross_validation:
        features_train, labels_train = features[train], labels[train]
        features_test, labels_test = features[test], labels[test]

        classifier = LogisticRegression()
        classifier.fit(features_train, labels_train)

        score = classifier.score(features_test, labels_test)
        if score > best_score:
            best_score = score
            result = classifier

    return result