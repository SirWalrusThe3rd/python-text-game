#pylint:disable=W0312
from items import *
import random

class Hero:
   
    def __init__(self, name, lvl = 0):
        self.name = name
        self.currency = {"Gold":0, "Silver":4, "Copper":45}
        self.lvl = lvl
        self.stats = {"Health":100, "Stamina":100, "Mana":25}
        self.attributes = 30
        self.inventory = [stick]
        self.equipped = self.inventory[0]
        self.ability = {"slap":12, "stab":self.equipped.deal_dmg()+ 6, "slash":self.equipped.deal_dmg() + 10, "flee":self.attributes}

    def __repr__(self):
        return self.inventory   

    def get_name(self):
        return self.name
            
    def get_equipped(self):
        return self.equipped

    def get_money(self):
        goldbag = [[i,e] for i,e in self.currency.items()]
        return goldbag

    def get_inventory(self):
        n = 0
        for i in self.inventory:
            n += 1
            return "{n}:{i}".format(n = n, i = i.get_name())

    def get_ability(self):
        return self.ability
    
    def special(self,ability):
        pass
        
    def get_health(self, minus = None, add = None):
        if minus:
            self.stats["Health"] -= minus
        elif add:
            self.stats["Health"] += add
        else:
            return self.stats.get("Health")
        
        
    def get_stam(self, minus = None, add = None):
        if minus:
            self.stats["Stamina"] -= minus
        elif add:
            self.stats["Stamina"] += add
        else:
            return self.stats.get("Stamina")
    
    def add_items(self, start_items):
        for items in start_items:
            self.inventory.append(items)
    
    def add_attribute(self, start_class):
        for attribute in start_class:
            self.attributes.append(attribute)               


class Enemy:
    
    def __init__(self, name, weapon = stick, health = 45, stamina = 50, mana = 10, lvl = 0):
        self.health = health
        self.stamina = stamina
        self.mana = mana
        self.lvl = lvl
        self.name = name
        self.weapon = weapon
        
    def get_name(self):
        return self.name
    
    def get_health(self, minus = None, add = None):
        if minus:
            self.health -= minus
        elif add:
            self.health += add
        else:
            return self.health

    def get_stam(self, minus = None, add = None):
    
        if minus:
            self.stamina -= minus
        elif add:
            self.stamina += add
        else:
            return self.stamina   

    def get_weapon(self):
        return self.weapon.get_all()
    
    def get_weapon_dmg(self):
        return self.weapon.deal_dmg()
    
    
