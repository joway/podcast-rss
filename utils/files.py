import json


def read_json(filename):
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except:
            return []


def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
