from stack_overflow_center.data_extractor.xml_to_tsv_and_json_converter import convert

def extract_posts_data(src, tsv_dest, json_dest, parse_function):
        convert(src, tsv_dest, json_dest, parse_function)