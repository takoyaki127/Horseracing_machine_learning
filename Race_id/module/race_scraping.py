from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# ブラウザの設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--log-level=3')

driver = webdriver.Chrome(
    '../chromedriver_win32/chromedriver.exe', options=options)
driver.implicitly_wait(10)


# 開催日からレースのURLをスクレイピング
# chromeドライバを'./chromedriver_win32/chromedriver.exe'に入れてください。
# ※　time.sleep()を使ってください。
def day_to_raceID(url):
    url = url

    driver.get(url)

    a_tags = driver.find_elements(
        By.XPATH, "//dd[@class='RaceList_Data']/ul/li/a[@class='']")
    race_url = [x.get_attribute('href') for x in a_tags]

    race_ids = list(map(url_to_raceID, race_url))

    return race_ids


def url_to_raceID(url):
    # s = 'https://race.netkeiba.com/race/result.html?race_id=201806050212&rf=race_list'
    m = re.search(r'race_id=[0-9]*', url)
    race_id = m.group()[8:]

    return race_id


def driver_close():
    driver.close()
