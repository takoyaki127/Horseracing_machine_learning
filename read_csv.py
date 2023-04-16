import csv

from scraping import scraping_result


def read_csv(file_path):
    # './race_id_(2023, 1)_(2023, 3).csv'
    with open(file_path, 'r') as f:
        render = csv.reader(f)
        race_ids: list[str] = []
        for x in render:
            race_ids.extend(x)

    return race_ids
