from module.create_url import create_calender_URL
from module.date_scraping import calender_to_event_date_link
from module.race_scraping import day_to_raceID
import time
import csv

# 開催日程のURLを生成   (year_start,year_end,month_start=1,month_end=12)
calender_url = create_calender_URL(2018, 2018, 12, 12)

# 開催レース一覧のURLを生成
event_url = []
for event_day in calender_url:
    event_url.extend(calender_to_event_date_link(event_day))
    time.sleep(0.5)

# レースIDを生成
race_ids = []
for ele in event_url:
    race_ids.extend(day_to_raceID(ele))
    time.sleep(0.2)

# ファイル書き込み
with open('Race_URL.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(race_ids)
