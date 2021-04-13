import wallet
import game
import bet

class BlackjackApp:
    def __init__(self):
        self._wallet = Wallet()
        self._bet = 0
    
    def set_bet(self):
        self.bet = Bet()

    def start_new_game(self):
        self._wallet.take_bet(self._bet)
        Game(self._wallet,self._bet)