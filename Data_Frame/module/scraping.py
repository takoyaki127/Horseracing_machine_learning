import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(
    '../chromedriver_win32/chromedriver.exe', options=options)
driver.implicitly_wait(10)


def scraping_result(race_id):
    url = f"https://race.netkeiba.com/race/result.html?race_id={race_id}&rf=race_list"
    dfs = pd.read_html(url)

    mileage = serch_mileage(url)
    df = dfs[0]
    df = add_mileage(df, mileage)

    return df


def add_mileage(df: DataFrame, mileage):
    horse_num = df.shape[0]
    mileage_series = pd.Series(data=[mileage] * horse_num, name='距離')
    df = pd.concat([df, mileage_series], axis='columns')

    return df


def serch_mileage(url):

    driver.get(url)

    ele = driver.find_elements(By.XPATH, "//div[@class='RaceData01']")
    infos = ele[0].text.split('/')
    mileage = re.search(r'[0-9]+', infos[1])

    # driver.close()

    return int(mileage.group())
