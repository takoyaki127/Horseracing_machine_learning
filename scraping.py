import pandas as pd

from result import Result


def scraping_result(race_id):
    url = f"https://race.netkeiba.com/race/result.html?race_id={race_id}&rf=race_list"
    dfs = pd.read_html(url)
    df = dfs[0]

    return Result(df)
