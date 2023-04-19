from module.scraping import Chrome
from module.csv_manager import CsvManager
import pandas as pd
from tqdm import tqdm

# 読み込むcsvファイル
file_path = './csv/Race_ID/2023-1_2023-3.csv'
race_ids = CsvManager.read(file_path)

# list[DataFrame]を生成
browser = Chrome()
results = []
for id in tqdm(race_ids):
    results.append(browser.scraping_result(id))
browser.close()

# DataFrameを結合
df = pd.concat(results, ignore_index=True)

# DataFrameをcsvファイルで出力
CsvManager.output_DataFrame(df)
