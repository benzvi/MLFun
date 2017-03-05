from django.conf import settings

from stack_overflow_center.questions_classifier.classifier_repository import save
from stack_overflow_center.questions_classifier.data_extractor import extract_data
from stack_overflow_center.questions_classifier.label_decider import calculate_questions_labels
from stack_overflow_center.questions_classifier.trainers.logistic_regression_trainer import train
from stack_overflow_center.questions_classifier.feature_extractor import extract_questions_features


def classify():
    data = extract_data(settings)
    questions_features = extract_questions_features(data)
    questions_labels = calculate_questions_labels(data)
    classifier = train(questions_features, questions_labels)
    save(classifier)
