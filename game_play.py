from shares import Shares
from player import Player
import datetime
import time

class Game_play:
    def __init__(self):
        
        # Instantiate the Shares class.
        self.nvidia = Shares('NVidia', 3, 163.00, 164.00, 0.9)
        self.tsm = Shares('TSM', 1, 73.83, 73.85, 0.8)
        self.qualcomm = Shares('Qualcomm', 2, 121.42, 121.52, 0.5)

        self.companies = [self.nvidia, self.tsm, self.qualcomm]
        
        # Activate game, instantiate Player class and display share prices changes.
        self.active = True
        self.player_input = input('Enter your name. ')
        self.player = Player(self.player_input)
        self.display_share_prices()
     
    def control(self):
        if self.player_input == 'q':
            self.active = False
            print(f'Goodbye, {self.player.name}, hope to see you soon.')
        elif self.player_input == 'b':

            self.player_input = input('Which company`s shares do you wish to buy? TSM (1), Qualcomm (2) or Nvidia (3)')
            for company in self.companies:
                if self.player_input == str(company.id):
                    self.player_input = input(f'You have chosen to buy shares in {company.co_name}. The offer is ${company.offer:,.2f}. How many shares do you wish to buy?')
                    transaction_value = int(self.player_input) * company.offer
                    self.player.transaction['company_name'] = company.co_name
                    self.player.transaction['no_of_shares'] = self.player_input
                    self.player.transaction['price'] = company.offer
                    self.player.transaction['tran_type'] = 'buy'
                    self.player.transaction['time_stamp'] = datetime.datetime.now()
                    print(f'{self.player.name}, we confirm you bought { self.player.transaction["no_of_shares"] } shares at ${self.player.transaction["price"]:,.2f} per share at {self.player.transaction["time_stamp"]}. ')
                    self.player.tran_log.append(self.player.transaction)
                    self.player.cash_account -= transaction_value
                    print(f'Your cash account now has a value of ${self.player.cash_account:,.2f}. Press "space" to continue.' )
                    self.display_share_prices()                       
        

        elif self.player_input == 'b':
            input('How many shares do you want to sell')
        elif self.player_input == 'w':
            print('play on')
            self.display_share_prices()
        elif self.player_input == 'p':
            print(f'{self.player.name}`s portfolio as at {datetime.datetime.now()}')
            print(self.player.tran_log)
            time.sleep(5)
            self.display_share_prices()
            self.player_input = input('buy, s: sell, w: wait, p to view your portfolio at this valuation or q: quit. ' )
    

    def display_share_prices(self):
        for i in range(50):
            time.sleep(0.01)
            self.nvidia.update_share_price()
            self.tsm.update_share_price()
            self.qualcomm.update_share_price()
            print('Welcome to Stocks n Stonkers, ' + self.player.name + '. The markets are open for trading.')
            print("You have a cash balance of ${:,.2f}".format(self.player.cash_account))
            print("Semi conductor Manufacturer share prices (USD $)")
            print("")
            print("")
            print(f'{self.qualcomm.co_name} share price-  bid: ${self.qualcomm.bid:,.2f}, offer: ${self.qualcomm.offer:,.2f}')
            print(f'{self.tsm.co_name} share price-       bid: ${self.tsm.bid:,.2f},  offer: ${self.tsm.offer:,.2f}')
            print(f'{self.nvidia.co_name} share price-    bid: ${self.nvidia.bid:,.2f}, offer: ${self.nvidia.offer:,.2f}')
            print("")
            print("")
        self.player_input = input('buy, s: sell, w: wait, p to view your portfolio at this valuation or q: quit. ' )
        self.control()
