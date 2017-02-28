import json


tags_data = {}

def get_tags_data(path):
    global tags_data

    if tags_data and tags_data.has_key(path):
        return tags_data[path]
    else:
        with open(path) as json_file:
            tags_data[path] = json.load(json_file)
            return tags_data[path]