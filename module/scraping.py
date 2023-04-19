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

    def scraping_result(self, race_id):
        url = f"https://race.netkeiba.com/race/result.html?race_id={race_id}&rf=race_list"
        dfs = pd.read_html(url)

        # 距離のSeriesを結合
        mileage = self.serch_mileage(url)
        df = dfs[0]
        df = add_mileage(df, mileage)

        return df


# 距離のSeriesを結合
def add_mileage(df: DataFrame, mileage):
    horse_num = df.shape[0]
    mileage_series = pd.Series(data=[mileage] * horse_num, name='距離')
    df = pd.concat([df, mileage_series], axis='columns')

    return df
