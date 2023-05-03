import pandas as pd
from tqdm import tqdm
from pandas import DataFrame

from module.scraping import Chrome
from module.csv_manager import CsvManager

from module.file_list import uncreated_files
from module.multi_thread import MultiThread


def main(file_path):
    # 読み込むcsvファイル
    # file_path = './csv/Race_ID/2023-1_2023-3.csv'
    file_path = file_path
    race_ids = CsvManager.read(file_path)
    print(file_path)

    # list[DataFrame]を生成
    browser = Chrome()
    results: list[DataFrame] = []
    for id in tqdm(race_ids):
        results.append(browser.scraping_result(id))
    browser.close()

    # DataFrameを結合
    df = pd.concat(results, ignore_index=True)

    # DataFrameをcsvファイルで出力
    CsvManager.output_DataFrame(df, file_path)


if __name__ == "__main__":
    threads = MultiThread(main, uncreated_files())
    threads.start(3)

    print('finish')
