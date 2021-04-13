import deck
import hand
import wallet

class Game:
    def __init__(self,wallet,bet):
        self._player_hand = Hand()
        self._dealer_hand = Hand()
        self._deck = Deck()
        self._wallet_in_use = wallet
        self._bet = bet

    def start():
        self._player_hand.add_card(self._deck)
        self._dealer_hand.add_card(self._deck)
        self._player_hand.add_card(self._deck)
    
    def add():
        hand.add_card()
        if _player_hand.is_over() > 21:
            return ["lost"]
        elif _player_hand.get_sum() == 21:
            self.stand()
        elif 9 <= _player_hand.get_sum() <= 11:
            return ["stand","add","double"]
        else: return ["stand","add"]

    def stand():
        if self._player_hand.is_blackjack() and self._dealer_hand.get_sum() < 10:
            self._wallet_in_use.blackjack(self._bet)
            return ["win"]
        while self._dealer_hand.get_sum() < 17:
            self._dealer_hand.add_card()
        if self._dealer_hand.is_over():
            if self._player_hand.is_blackjack():
                self._wallet_in_use.blackjack(self._bet)
                return ["win"]
            else: 
                self._wallet_in_use.double_back(self._bet)
                return ["win"]
        elif self._player_hand.get_sum() == self._dealer_hand.get_sum():
            return self._is_tie()
        elif self._player_hand.get_sum() != self._dealer_hand.get_sum():
            return self._is_different()
        
    def double():
        self._player_hand.add_card()
        self.stand()

    def surrender():
        if self._player_hand.get_number == 2:
            self._wallet_in_use.half_back(self._bet)
            return ["half_pack"]
    
    def _is_tie(self):
        if self._player_hand.is_blackjack() and not self._dealer_hand.is_blackjack():
            self._wallet_in_use.blackjack()
        elif not self._player_hand.is_blackjack() and self._dealer_hand.is_blackjack():
            return ["lost"]
        elif self._player_hand.is_21() and self._dealer_hand.is_21():
            self._wallet_in_use.tie(self._bet)
            return ["tie"]
        else:
            return ["lost"]

    def _is_different(self):
        if self._player_hand.is_blackjack():
            self._wallet_in_use.blackjack(self._bet)
            return ["win"]
        elif self._player_hand.is_21() or self._player_hand.get_sum() > self._dealer_hand.get_sum():
            self._wallet_in_use.double_back(self._bet)
            return ["win"]
        else:
            return ["lost"]