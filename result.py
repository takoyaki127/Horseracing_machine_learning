from pandas import DataFrame


class Result():
    def __init__(self, df: DataFrame):
        df = df
        self.horse_num = df.shape[0]

        # 属性を抽出
        attribute = ['馬名', '性齢', '斤量', '騎手', 'タイム', '厩舎', '馬体重 (増減)']
        selected_df = df.loc[:, attribute]

        # 馬ごとのlist[Series]を生成
        self.status = []
        for i in range(self.horse_num):
            self.status.append(selected_df.iloc[i,])

        print(self.status[0])

        pass
