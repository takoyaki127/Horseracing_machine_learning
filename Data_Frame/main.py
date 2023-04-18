from module.scraping import scraping_result, driver_close
from module.csv_manager import read_csv, df_to_csv
import pandas as pd
from tqdm import tqdm

# 読み込むcsvファイル
file_path = './csv/Race_ID/2023-1_2023-3.csv'
race_ids = read_csv(file_path)

# list[DataFrame]を生成
results = []
for id in tqdm(race_ids):
    results.append(scraping_result(id))
driver_close()

# DataFrameを結合
df = pd.concat(results, ignore_index=True)

# DataFrameをcsvファイルで出力
df_to_csv(df)
