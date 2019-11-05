import json


def get_data():
    try:
        with open("data.json") as file:
            return json.load(file)
    except ValueError:
        raise Exception('data.json is inconsistent or missing')
