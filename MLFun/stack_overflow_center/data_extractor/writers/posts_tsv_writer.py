from stack_overflow_center.data_extractor.writers.base_writer import BaseWriter


class PostsTSVWriter(BaseWriter):

    def write(self, analysed_post):
        line = "\t".join(map(str, [analysed_post.id, analysed_post.flat_body]))
        self.file.write(line + "\n")

    def done(self):
        self.file.flush()
        self.file.close()
