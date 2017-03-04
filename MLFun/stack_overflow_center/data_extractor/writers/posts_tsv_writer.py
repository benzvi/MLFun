from stack_overflow_center.data_extractor.writers.base_writer import BaseWriter


class PostsTSVWriter(BaseWriter):

    def write(self, analyzed_post):
        line = "\t".join(map(str, [analyzed_post.id, analyzed_post.flat_body]))
        self.file.write(line + "\n")

    def done(self):
        self.file.flush()
        self.file.close()
