import json


def convert(from_path, to_path, to_json_path, parse_function):
    json_data = {}
    with open(to_path, "w") as f:
        for values in parse_function(from_path):
            id = values[0]
            text = values[1]

            line = "\t".join(map(str, [id, text]))
            f.write(line + "\n")

            json_data[id] = {
                'WordsCount': values[2],
                'CodeLinesCount': values[3],
                'AvgSentenceLength': values[4],
                'AvgWordLength': values[5],
                'CapsCount': values[6],
                'ExclamsCount': values[7],
                'ImagesCount': values[8],
                "Score": values[9],
                "TitleWordsCount": values[10],
                "TotalTagsCount": values[11],
                "AnswerCount": values[12],
                "CommentCount": values[13],
                "FavoriteCount": values[14]
            }

    with open(to_json_path, "w") as json_file:
        json.dump(json_data, json_file)
