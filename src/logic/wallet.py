import sqlite3

class Wallet:
    def __init__(self):
        _con = sqlite3.connect('data.db')
        _cur = _con.cursor()
        _cur.execute('''CREATE TABLE wallet (amount integer, games integer, wins integer)''')
        _cur.execute('''INSERT INTO wallet VALUES (1000,0,0)''')
        _con.commit()
        _con.close()
    
    def take_bet(self,bet):
        _con = sqlite3.connect('data.db')
        _cur = _con.cursor()
        _amount = _cur.execute('''SELECT amount FROM wallet''')
        if _amount >= bet and bet >=10 and bet <= 1000:
            _query = '''UPDATE wallet SET amount = ?'''
            _cur.execute(_query,_amount-bet)

        _amount_games = '''SELECT games FROM wallet'''
        _query_games = '''UPDATE wallet SET games = ?'''
        _cur.execute(_query_games,_amount_games+1)

        _con.commit()
        _con.close()
        
    
    def half_back(self,bet):
        _con = sqlite3.connect('data.db')
        _cur = _con.cursor()
        _amount_amount = _cur.execute('''SELECT amount FROM wallet''')
        _query_amount = '''UPDATE wallet SET amount = ?'''
        _cur.execute(_query_amount,_amount+(bet//2))
        _con.commit()
        _con.close()
    
    def tie(self,bet):
        #self._wallet += bet
    
    def double_back(self,bet):
        #self._wallet += (bet*2)

    def blackjack(self,bet):
        #self._wallet += int(bet*2.5)
    
    def check_wallet(self):
        #if self._wallet == 0:
        #    self._wallet = 1000