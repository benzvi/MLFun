import json


def convert(from_path, to_path, parse_function):
    result = {}
    with open(to_path, "w") as json_file:
        for tag_name, tag_count in parse_function(from_path):
            result[tag_name] = tag_count

        json.dump(parse_function(from_path), json_file)