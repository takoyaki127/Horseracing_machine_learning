import pandas as pd

from result import Result


def scraping_result(race_id, scores: list[Result]):
    url = f"https://race.netkeiba.com/race/result.html?race_id={race_id}&rf=race_list"
    dfs = pd.read_html(url)
    df = dfs[0]

    for i in range(df.shape[0]):

        rank = df["着 順"][i]
        horse_name = df['馬名'][i]
        jockey = df['騎手'][i]

        flag = False
        for ele in scores:
            if ele.horse_name == horse_name and ele.jockey == jockey:
                ele.add_score(rank)
                # ele.count_up()
                flag = True
                break

        if flag == False:
            scores.append(Result(rank, horse_name, jockey))

    return scores


# url = "https://db.netkeiba.com/race/202306010611/"
# scores = []
# scores = scraping_result(url, scores)

# for ele in scores:
#     print(ele.get_score())
