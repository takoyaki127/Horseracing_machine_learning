import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class Chrome():
    # ブラウザの設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--log-level=3')

    def __init__(self):
        self.driver = webdriver.Chrome(
            '../chromedriver_win32/chromedriver.exe', options=Chrome.options)
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.close()

    # 距離の取得
    def serch_mileage(self, url):
        self.driver.get(url)

        ele = self.driver.find_elements(By.XPATH, "//div[@class='RaceData01']")
        infos = ele[0].text.split('/')
        mileage = re.search(r'[0-9]+', infos[1])

        return int(mileage.group())

    def scraping_result(self, race_id) -> DataFrame:
        url = f"https://race.netkeiba.com/race/result.html?race_id={race_id}&rf=race_list"
        dfs = pd.read_html(url)

        # 距離のSeriesを結合
        mileage = self.serch_mileage(url)
        df = dfs[0]
        df = add_mileage(df, mileage)

        df = grade_list(df)
        df = second_float_list(df)

        return df


# 距離のSeriesを結合
def add_mileage(df: DataFrame, mileage):
    horse_num = df.shape[0]
    mileage_series = pd.Series(data=[mileage] * horse_num, name='距離')
    df = pd.concat([df, mileage_series], axis='columns')

    return df


# 順位のSeriesを変換
def grade_list(df: DataFrame):
    rank_list = [rank_to_grade(rank) for rank in df['着 順']]
    rank_series = pd.Series(rank_list)
    df['着 順'] = rank_series
    return df


# 1~3 -> 0
# 4~6 -> 1
# None -> -1
def rank_to_grade(n):
    try:
        return int(int(n) / 3)
    except Exception as e:
        return -1


# タイムのSeriesを変換
def second_float_list(df: DataFrame):
    sec_list = [time_to_second(time) for time in df['タイム']]
    sec_series = pd.Series(sec_list)
    df['タイム'] = sec_series
    return df


def time_to_second(time_str: str):
    try:
        minutes, second = time_str.split(':')
        time_float = float(minutes) * 60 + float(second)
        return time_float
    except Exception as e:
        return -1.0
