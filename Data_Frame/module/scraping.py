import pandas as pd
from pandas import DataFrame


def scraping_result(race_id):
    url = f"https://race.netkeiba.com/race/result.html?race_id={race_id}&rf=race_list"
    dfs = pd.read_html(url)
    df = dfs[0]
    df = add_mileage(df, 10)

    return df


def add_mileage(df: DataFrame, mileage):
    horse_num = df.shape[0]
    mileage_series = pd.Series(data=[mileage] * horse_num, name='距離')
    df = pd.concat([df, mileage_series], axis='columns')

    return df
