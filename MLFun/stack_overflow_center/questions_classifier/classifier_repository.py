import pickle


def save(classifier):
    pickle.dump(classifier, open("questions_classifier.dat", "w"))


def load():
    return pickle.load(open("questions_classifier.dat", "r"))