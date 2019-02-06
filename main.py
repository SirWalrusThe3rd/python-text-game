#pylint:disable=W0312
#this is my first python game
from characters_n_enemies import *

goblin = Enemy("Goblin")
demon = Enemy("Demon")

def get_answer(q1 = None, q2 = None, q3 = None, q4 = None):

	    choice = " "
	    
	    while choice:
		    choice = input("\n:").strip(" ")
		    if not choice:
			    print("Nothing happend.\ntry again.\n")
		    elif choice == q1:
			    return q1
		    elif choice == q2:
			    return q2
		    elif choice == q3:
			    return q3
		    elif choice == q4:
			    return q4
		    else:
			    print("\ntry again.\n")
		    choice = " "
		        
            
def attack_scr(player):
	abilities = [[ability, cost] for ability, cost in player.get_ability().items()]
	print("a)slap b)stab c)slash d)flee")
	a = None
	b = None
	c = None
	d = None
	for ability in abilities:
		if a == None:
			a = ability[0]
		elif b == None:
			b = ability[0]
		elif c == None:
			c = ability[0]
		elif d == None:
			d = ability[0]
		else:
			break
	move = get_answer(a, b, c, d)
	return move
            
            
def battle(player, enemy, first):
	print("*******************************************************")
	print("\t\tBattle start\n \t\t{u} vs. {e}".format(u = player.get_name(), e = enemy.get_name()))
	input("*******************************************************\n\n")

	while int(player.get_health()) > 0 and int(enemy.get_health()) > 0:
		if first == 1:
			first +=1
			print("\nYour attack\n\nHEALTH\tSTAMINA")
			print(str(player.get_health())+"\t"+str(player.get_stam()))
			attack = attack_scr(player)
			
			if player.get_ability()[attack] <= player.get_stam():
				print(player.get_ability()[attack])
				player.get_stam(player.get_equipped().take_stam())
				enemy.get_health(player.get_ability()[attack])
				
				input("\nStamina:"+str(player.get_stam()))
				input("\nHealth enemy:\n"+ str(enemy.get_health()))
			
			else:
				print("you've run out of stamina you pass out\n\n\nGAME OVER")
	
			
		elif first == 2:
			first -= 1
			print("\n{e} attacks".format(e = enemy.get_name()))
			player.get_health(enemy.get_weapon_dmg())
			input(enemy.get_weapon_dmg())
			input("\nHealth:"+str(player.get_health()))
			if player.get_health() <= 0:
				print("YOU DIED\n\n\nGAME OVER!")

				
				
				
			
			      
			      
			      
		else:
			      print("battle error\n restart game")
	print("you won!" )
			     
		      

	
	      
	
        
 
def start():
    print("Are you ready to start?\ny/n")
    get_answer("y")
    player = Hero(input("Welcome adventure to the world\n\tKazur!\n\nMay I ask you your name?\n:"))
    
    print("\n\nGreat name! "+str(player.get_name())+" I think I have a cousin with that name.\nSpeaking of names my name is Gilfend")
    input()
    print("okay lets looks at your inventory\n\n" + str(player.get_inventory()))
    input()
    print("\n\nReally all you got is a twig that i just watched you pick up.\nWhatever we'll find you some more how much gold do you have?\n\n")
    input()
    print(player.get_money())
    input()
    print("\nLooks like your broke;Should of guessed...\nWell tell you what when we get to town ill buy you\none thing.\nnow were are we again?\n\n")
    input()
    print("{name}:\na:I dont know I thought you knew.\tb:Who knows lets just follow the trail\n\n\n".format(name = player.get_name()))
    chosen = get_answer("a", "b")
    
    if chosen == "a":
          print("\nNo im kinda lost. \no'well lets just follow this trail.")
          
    elif chosen == "b":
          print("Well at least your trying to help.\nSure that sounds like a great idea!")
         
    else:
        print("start Error")
    input()
    print("\n\nyour following the trail till a nasty goblin pops out oh no!\n\n all you got is your twig to fight\n(Gilfend is cowering in the corner)\n\n")
    battle(player, goblin,1)
    print("\n\n\nLooks like you got some moves I was just holding back wanted you to learn is all")
    print("{name}:\na)Sure that\'s what you were doing\tb)sure but next time maybe help?".format(name = player.get_name()))
    chosen = get_answer("a", "b")
    if chosen == "a":
	    print("\nOf course it was any way lets continue")
    else:
	    print("Maybe but you should just tough it up and let\'s go")
    print("\n\nyou've arived at a small village\n\nRemember I said I would get you one thing only so were too\n\n\ta)Armor shop\tb)Weapon shop\tc)Magic shop")
    chosen = get_answer("a", "b", "c")
    print("\n\nto bad game is over you suck!!!!!")


          
    
#start of game
start()
