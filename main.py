from scraping import scraping_result
from read_csv import read_csv


file_path = './race_id_(2023, 1)_(2023, 3).csv'
race_ids = read_csv(file_path)

scores = []
for id in race_ids:
    scraping_result(id, scores)
