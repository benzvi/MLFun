from stack_overflow_center.data_extractor.xml_parser import parse_xml

TSV_FILE = "stack_overflow_questions.tsv"

def convert_xml_to_tsv(path):

    with open(TSV_FILE, "w") as f:
        for values in parse_xml(path):
            line = "\t".join(map(str, values))
            f.write(line + "\n")