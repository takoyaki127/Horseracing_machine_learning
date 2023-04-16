class Result():
    def __init__(self, rank, name, jockey):

        self.horse_name = name
        self.jockey = jockey
        try:
            self.rank_sum = int(rank)
            self.count = 1
        except:
            print('Rank_エラー')
            self.rank_sum = 0
            self.count = 0

    def count_up(self):
        self.count += 1

    def add_score(self, rank):
        try:
            self.rank_sum += int(rank)
            self.count_up()
        except:
            print('Add_エラー')

    def get_score(self):
        return self.rank_sum / self.count
