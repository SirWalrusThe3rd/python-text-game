#this is a module for stores and locations
from items import *
class Store:

    def __init__(self, name, store_inv = []):
        self.name = name
        self.store_inv = store_inv

    def get_store_inv(self):
        return self.store_inv
    
    def get_price(self, choice):
        return self.store_inv[choice].get_item_price()

#class Magic_shop(Store):

#    def __init__(self, store_inv = [low_health_pot, low_stamina_pot, low_mana_pot]):
    

