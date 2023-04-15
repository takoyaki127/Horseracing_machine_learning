import time


# ※　time.sleep()を使ってください。
def create_calender_URL(year_start, year_end, month_start=1, month_end=12):
    # https://race.netkeiba.com/top/calendar.html?year=2015&month=7
    url_head = 'https://race.netkeiba.com/top/calendar.html?'

    year = [year_start, year_end]
    month = [month_start, month_end]

    url_list = []
    for i in range(year[1]-year[0]+1):
        year_str = f"year={year[0] + i}"

        for k in range(month[1]-month[0]+1):
            month_str = f"month={month[0]+k}"
            date = year_str + "&" + month_str

            url = url_head + date
            print(url)
            url_list.append(url)

    return url_list
