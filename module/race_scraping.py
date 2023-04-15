from selenium import webdriver
from selenium.webdriver.common.by import By


# 開催日からレースのURLをスクレイピング
# chromeドライバを'./chromedriver_win32/chromedriver.exe'に入れてください。
# ※　time.sleep()を使ってください。
def day_to_race(url):
    url = url

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(
        './chromedriver_win32/chromedriver.exe', options=options)
    driver.implicitly_wait(10)
    driver.get(url)

    a_tags = driver.find_elements(
        By.XPATH, "//dd[@class='RaceList_Data']/ul/li/a[@class='']")
    race_url = [x.get_attribute('href') for x in a_tags]

    return race_url
