import requests
from bs4 import BeautifulSoup
import lxml


# カレンダーから開催日のURLをスクレイピング
def calender_to_event_date_link(url):
    url = url

    res = requests.get(url)

    # 'html.parser'
    soup = BeautifulSoup(res.text, 'lxml')

    td_tags = soup.find('tbody')
    a_tags = td_tags.find_all('a')

    url_list: list[str] = [x['href'] for x in a_tags]

    url_head = "https://race.netkeiba.com"
    arrange_url_list = [x.replace("..", url_head) for x in url_list]

    return arrange_url_list
