import deck

class Hand:
    def __init__(self):
        self._sum = 0
        self._number = 0
        self._all_cards = []
    
    def add_card(self,deck):
        card = deck.deal()
        self._sum += card[0]
        self._number += 1
        self._all_cards.append(card)

    def get_sum(self):
        return self._sum

    def get_number(self):
        return self._number
    
    def get_all_cards(self):
        return self._all_cards
    
    def is_blackjack(self):
        if self._sum == 21 and self._number == 2:
            return True
        else: return False
    
    def is_21(self):
        if self._sum == 21:
            return True
        else: return False
    
    def is_over(self):
        if self._sum > 21:
            return True
        else: return False