import csv
from pandas import DataFrame
import re


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
    def output_DataFrame(df: DataFrame, file_name, header=True):
        file_name = extract_filename_parts(file_name)
        df.to_csv(f'./csv/Result/{file_name}.csv', mode='a', header=header)


def extract_filename_parts(path):
    return re.search("[0-9]*-[0-9]*_[0-9]*-[0-9]*", path).group()
