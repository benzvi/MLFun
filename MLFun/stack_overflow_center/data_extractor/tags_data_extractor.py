from stack_overflow_center.data_extractor.xml_to_json_converter import convert

def extract_tags_data(src, dest, parse_function):
    convert(src, dest, parse_function)
