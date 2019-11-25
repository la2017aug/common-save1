import json


DB = {}

with open('db/db_file.json') as db_file:
    DBfile = json.load(db_file)
