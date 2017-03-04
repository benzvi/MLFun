import numpy

from stack_overflow_center.questions_classifier.feature import Feature

INCLUDED_FEATURES = [
    Feature.WORDS_COUNT.value,
    Feature.CODE_LINES_COUNT.value,
    Feature.AVERAGE_SENTENCE_LENGTH.value,
    Feature.AVERAGE_WORD_LENGTH.value,
    Feature.CAPS_COUNT.value,
    Feature.EXCLAMS_COUNT.value,
    Feature.IMAGES_COUNT.value,
    Feature.TITLE_WORDS_COUNT.value,
    Feature.TOTAL_TAGS_COUNT.value
]


def extract_questions_features(data):
    return numpy.array([feature[INCLUDED_FEATURES] for feature in data])