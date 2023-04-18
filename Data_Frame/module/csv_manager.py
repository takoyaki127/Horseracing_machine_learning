import csv
from pandas import DataFrame


# csvファイルを読み込んで、list[str]を返す
def read_csv(file_path):
    # './race_id_(2023, 1)_(2023, 3).csv'
    with open(file_path, 'r') as f:
        render = csv.reader(f)
        race_ids: list[str] = []
        for x in render:
            race_ids.extend(x)

    return race_ids


# DataFrameをcsvに書き込む
def df_to_csv(df: DataFrame, header=False):
    df.to_csv('./csv/Result/data.csv', mode='a', header=header)
