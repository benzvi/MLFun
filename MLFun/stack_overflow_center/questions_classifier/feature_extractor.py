import numpy

from stack_overflow_center.common import features_indices

INCLUDED_FEATURES = [
    features_indices.WORDS_COUNT,
    features_indices.CODE_LINES_COUNT,
    features_indices.AVERAGE_SENTENCE_LENGTH,
    features_indices.AVERAGE_WORD_LENGTH,
    features_indices.CAPS_COUNT,
    features_indices.EXCLAMS_COUNT,
    features_indices.IMAGES_COUNT,
    features_indices.TITLE_WORDS_COUNT,
    features_indices.TOTAL_TAGS_COUNT
]


def extract_questions_features(data):
    return numpy.array([feature[INCLUDED_FEATURES] for feature in data])
