import csv

with open('./Race_URL.csv', 'r') as f:
    render = csv.reader(f)
    race_ids: list[str] = []
    for x in render:
        race_ids.extend(x)
