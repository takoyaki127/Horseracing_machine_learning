from module.scraping import scraping_result
from Data_Frame.module.read_csv import read_csv
import pandas as pd


file_path = './csv/race_id_(2023, 1)_(2023, 3).csv'
race_ids = read_csv(file_path)

results = []
for id in race_ids:
    results.append(scraping_result(id))

df = pd.concat(results, ignore_index=True)
