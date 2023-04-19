import csv
from pandas import DataFrame


class CsvManager():
    # csvファイルを読み込んで、list[str]を返す
    @staticmethod
    def read(file_path):
        # './race_id_(2023, 1)_(2023, 3).csv'
        with open(file_path, 'r') as f:
            render = csv.reader(f)
            race_ids: list[str] = []
            for x in render:
                race_ids.extend(x)
        return race_ids

    # DataFrameをcsvに書き込む
    @staticmethod
    def output_DataFrame(df: DataFrame, header=False):
        df.to_csv('./csv/Result/data.csv', mode='a', header=header)
