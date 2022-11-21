import datetime


class Player:
    def __init__(self, name):
        self.name = name
        self.cash_account = 10000
        self.transaction = {
            'company_name': 'null',
            'no_of_shares': 100,
            'price': 0,
            'tran_type': 'buy',
            'time_stamp': datetime.datetime.now()                        
        }
        self.tran_log = []
        

    def transaction(co_name, no_of_shares, price, tran_type, time_stamp):
        # calc the transaction value = no of shares x price.  Is it smaller than self.cash_account. 

        # deduct transaction from cash balance

        # insert values to self.transaction and then to self.tran_log
        pass


    def calc_portfolio_value():
        # loop through the transaction log taking company name and finding the current price, then multiply by the shares bought in the transaction. Total is the portfolio value
        pass

    def display_portfolio():
        # displays the share name, no of shares and the value of the shares in rows with a total
        pass

