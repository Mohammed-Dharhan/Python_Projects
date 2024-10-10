#Class to keep track of score

class Scoreboard:
    def __init__(self, capacity=10):
        self._board = [0] * capacity
        self._n = 0
        
    def __getitem__(self, k):
        return self._board[k]
    
    def __str__(self):
        return " ".join(str(self._board[k]) for k in range(self._n))
    
    def add(self, entry):
        self._board[self._n] = entry
        self._n += 1
        
        
def main():
    scores = Scoreboard(10)
    scores.add(100)
    scores.add(200)
    scores.add(300)
    print(scores)
    

if __name__ == "__main__":
    main()