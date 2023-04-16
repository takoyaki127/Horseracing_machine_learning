from pandas import DataFrame


class Result():
    def __init__(self, df: DataFrame):
        df = df
        self.status = df.loc[:, ['馬名', '性齢']]
        pass
