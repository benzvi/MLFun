from stack_overflow_center.data_extractor.pipes.base_pipe import BasePipe


class TitlePipe(BasePipe):

    @staticmethod
    def transform(parsed_object, result):
        result.title_words_count = len(parsed_object.title.split(" "))