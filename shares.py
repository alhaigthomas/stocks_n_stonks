
import time
import random

class Shares:
 
    def __init__(self, name, id, bid, offer, vol):
        self.co_name = name
        self.id = id
        self.bid = bid
        self.offer = offer
        self.volatility = vol

    def update_share_price(self):
        up_down = random.choice((-1,1))
        price_change = up_down * self.volatility/100
        share_bid = self.bid * (1 + price_change)
        share_offer = self.offer * (1 + price_change)
        self.bid = share_bid
        self.offer = share_offer
        
    def get_share_price(self, bid_or_offer):
        if bid_or_offer == 'bid':
            return self.bid

        elif bid_or_offer == 'offer':
            return self.offer

