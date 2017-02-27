from stack_overflow_center.data_extractor.pipes.tags_pipe import TagsPipe
from stack_overflow_center.data_extractor.pipes.title_pipe import TitlePipe
from stack_overflow_center.data_extractor.pipes.question_body_pipe import QuestionBodyPipe

PIPES = [TagsPipe, QuestionBodyPipe, TitlePipe]
