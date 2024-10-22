import json


def json_write_file(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def json_read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
