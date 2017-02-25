import json

def convert(from_path, to_path, to_json_path, parse_function):

    with open(to_path, "w") as f:
        for values in parse_function(from_path):
            if isinstance(values, dict):
                with open(to_json_path, "w") as json_file:
                    json.dump(values, json_file)
            else:
                line = "\t".join(map(str, values))
                f.write(line + "\n")
