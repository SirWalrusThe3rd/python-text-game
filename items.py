#pylint:disable=W0312
class Weapon:
    def __init__(self, name, dmg, stam, lvl, price = 0):
        self.name = name
        self.dmg = dmg
        self.stam = stam
        self.lvl = lvl
        self.price = price
        self.stats = [self.name, self.dmg, self.stam, self.lvl]

        
    def deal_dmg(self):
        return self.dmg
		
    def take_stam(self):
        return self.stam
	
    def check_lvl(self):
        return self.lvl

    def get_name(self):
        return self.name

    def get_item_price(self):
        return self.price

    def get_all(self):
        for i in self.stats:
            print(i)

greatsword = Weapon("Kingslayer", 12, 25, 1)

sword_1 = Weapon("Rusty shortsword", 6, 8, 3)

stick = Weapon("Twig", 4, 1, 0)

class Potion:

    def __init__(self, name, potentcy = "", price =0, extra_pts = 0):
        self.price = price
        self.name = name
        self.pts = extra_pts

        if potentcy == "low":
            self.pts += 15
        elif potentcy == "normal":
            self.price += 12
            self.pts += 25
        elif potentcy == "high":
            self.pts += 40
            self.price += 25
        else:
            return "Potion low,normal,high Invalid ERROR"


    def get_item_price(self):
        return self.price

    def add_pts(self):
        return self.pts


low_mana_pot = Potion("Small Mana Potion", "low", 15)
low_health_pot = Potion("Small Health Potion", "low", 20)
#low_stamina_pot = Potion("")
