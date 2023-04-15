class Result():
    def __init__(self, rank, name, jockey):
        self.rank_sum = rank
        self.horse_name = name
        self.jockey = jockey

        self.count = 1

    def count_up(self):
        self.count += 1

    def add_score(self, rank):
        self.rank_sum += rank

    def get_score(self):
        return self.rank_sum / self.count
