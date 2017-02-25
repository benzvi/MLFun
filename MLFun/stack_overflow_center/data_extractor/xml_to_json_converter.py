import json


def convert(from_path, to_path, parse_function):
    with open(to_path, "w") as json_file:
        json.dump(parse_function(from_path), json_file)