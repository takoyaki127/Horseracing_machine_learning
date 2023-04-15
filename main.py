from create_url import create_calender_URL
from date_scraping import calender_to_event_date_link
from race_scraping import day_to_race
import time

# 開催日程のURLを生成   (year_start,year_end,month_start=1,month_end=12)
calender_url = create_calender_URL(2018, 2018, 11, 12)

# 開催レース一覧のURLを生成
event_url = []
for event_day in calender_url:
    event_url.extend(calender_to_event_date_link(event_day))
    time.sleep(1)

# レースのURLを生成
url_list = []
for ele in event_url:
    url_list.extend(day_to_race(ele))
    time.sleep(1)

pass
