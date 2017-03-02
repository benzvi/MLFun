from stack_overflow_center.questions_classifier import classifier_repository


def predict(question):
    classifier = classifier_repository.load()
    return classifier.predict(question)
