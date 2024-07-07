class ScoreSheet:
    def __init__(self, score:list[int]):
        self._score_list:list[int] = score
    
    def add_score(self, score):
        self._score = score
        self._score_list.append(self._score)

    def average(self):
        sort = sorted(self._score_list)
        del sort[0]
        return sum(sort)/len(sort)

    def report(self):
        print(f'Scores : {self._score_list}')
        print(f'Average (excluding lowest score) : {self.average()}')

    def __str__(self) -> str:
        return f'{self.report()}'

def main():
    score = ScoreSheet([10,5,12])
    score.add_score(11)
    score.report()

if __name__=='__main__':
    main()