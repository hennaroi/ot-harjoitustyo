import pydealer

class Deck:
    def __init__(self):
        self._deck = pydealer.Deck()
        self._deck.shuffle()
    
    def deal(self):
        _card = str(self._deck.deal())
        _card_splitted = _card.split()
        _card_to_return = ()
        if _card_splitted[0] == 'Ace':
            _card_to_return = (1,_card_splitted[2])
        elif card_splitted[0] == 'Jack' or _card_splitted[0] == 'Queen' or _card_splitted[0] == 'King':
            _card_to_return = (10,_card_splitted[2])
        else:
            _card_to_return = (int(_card_splitted[0]),_card_splitted[2])
        return _card_to_return