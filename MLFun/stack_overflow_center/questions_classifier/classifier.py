
from django.conf import settings

from stack_overflow_center.questions_classifier.classifier_repository import save
from stack_overflow_center.questions_classifier.label_decider import calculate_questions_labels
from stack_overflow_center.questions_classifier.feature_extractor import extract_questions_features
from stack_overflow_center.questions_classifier.trainers.logistic_regression_trainer import train


def classify():
    questions_features = extract_questions_features(settings)
    questions_lables = calculate_questions_labels(questions_features)
    classifier = train(questions_features, questions_lables)
    save(classifier)