class Bet:
    def __init__(self):
        self._sum = 0
        self._bets = []
    
    def add_bet(self,bet):
        self._sum += bet
        self._bets.append(bet)
    
    def delete_bet(self):
        _to_delete = self._bets.pop()
        self._sum -= _to_delete