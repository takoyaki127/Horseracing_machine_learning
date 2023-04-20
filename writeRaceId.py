import time
import csv
from tqdm import tqdm

from module.create_url import create_calender_URL
from module.date_scraping import calender_to_event_date_link
from module.race_scraping import Chrome

# 日付の指定
year_start = 2016
year_end = 2016
month_start = 1
month_end = 12


# 開催日程のURLを生成   (year_start,year_end,month_start=1,month_end=12)
calender_url = create_calender_URL(
    year_start,
    year_end,
    month_start,
    month_end
)

# 開催レース一覧のURLを生成
event_url = []
for event_day in calender_url:
    event_url.extend(calender_to_event_date_link(event_day))
    time.sleep(0.5)

# レースIDを生成
browser = Chrome()
race_ids = []
for ele in tqdm(event_url):
    race_ids.extend(browser.day_to_raceID(ele))
    time.sleep(0)
browser.close()

# ファイル書き込み
file_name = f'csv/Race_ID/{year_start}-{month_start}_{year_end}-{month_end}.csv'
with open(file_name, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(race_ids)
