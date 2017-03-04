import numpy

SCORE = 7
ANSWER_COUNT = 10
FAVORITE_COUNT = 12


def calculate_questions_labels(questions):
    return numpy.asarray([_is_question_good(question) for question in questions])




def _is_question_good(question):
    return question[SCORE] > 2 or question[ANSWER_COUNT] > 2 or question[FAVORITE_COUNT] > 1
