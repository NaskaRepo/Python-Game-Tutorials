#	python tutorial_2.py
import os
import random

#
#	This function is responcible for character creation
#
def createCharacter():
	#	Clears the screen
	os.system('cls')
	
	#	Create an empty dictionary to hold the character's stats {key : value, key : value, key : value,...}
	stats = {}
		
	#	Create the key "hp" and set the value to 10
	#	stats = {"hp":10}
	stats["hp"] = 10
		
	#	Create the key "name" and set it to the player's input
	#	stats = {"hp":10,"name":<user input goes here>}
	stats["name"] = input("Please enter your name :  ")

	#
	#	TODO :  Add more stats
	#

	return stats


#
#	This function is responcible displaying the player's stats
#
def viewCharacter(player):
	#	Clears the screen
	os.system('cls')

	#	Remember player is just a dictionary of stats, key value pairs
	#	So for each key in the dictionary that is a player...
	for key in player:
		#	We get the value for that key and turn it into a string (text)
		value = str(player[key])

		#	Then we print the key, some fancy spacing, and the value
		print(key + "\t: " + value)

	#	Give the player a chance to read.  The \n means move the text to a new line
	input("\n-- Press enter to continue --")


#
#	This function is responcible handeling the player resting
#
def rest(player):
	#	Clears the screen
	os.system('cls')
	
	#	Let the player know they found a safe place to rest
	print("You found a safe place to rest for the night.")
	
	#	Check if the payer is hurt
	if player["hp"] < 10:
		#	Figure out how much hp is missing
		missingHp = 10 - player["hp"]

		#	Get a number between 1 and the amount of health missing
		healedHp = random.randint(1, missingHp)

		#	Add the healed amount to the player's hp
		player["hp"] += healedHp

		#	Let the player know how much they healed.  Had to convert the number healedHp to a string (text)
		print("You sleep peacefully though the night and healed " + str(healedHp) + " hp.")
	else:
		#	Just giving the player some feed back
		print("You sleep peacefully though the night.")

	#	Give the player a chance to read.  The \n means move the text to a new line
	input("\n-- Press enter to continue --")


#
#	This function is responcible handeling combat
#
def fight(player):
	#	Clears the screen
	os.system('cls')

	print("You get into a fight!")

	#
	#	TODO :  Add fight mechanics here
	#

	#	Give the player a chance to read.  The \n means move the text to a new line
	input("\n-- Press enter to continue --")


if __name__ == "__main__":
	#	Set the player variable equal to the return of the createCharacter function
	player = createCharacter()

	#	Keep looping through this code while the player has hp
	while player["hp"] > 0:
		#	Print out the options to the player
		print("Your options are...")
		print("1 - View Character")
		print("2 - Adventure")
		print("3 - Retire (Quit)")
		
		#	Get the player's choice
		choice = input("")

		#	The player wants to view their character so we'll call viewCharacter and pass in the player
		if choice == '1':
			viewCharacter(player)
		
		#	The player wants to adventure
		elif choice == '2':
			#	We create a variable called event and set it to a random number between 1 and 20
			event = random.randint(1, 20)
			
			#	If event is greater than 15 then the player gets to rest and we call the rest function and pass in the player 
			if event > 15:
				rest(player)
				
			#	If event is lower than 16 then the player gets into a fight
			else:
				fight(player)
				
			#
			#	TODO :  Add more events
			#		

		#	The player wants to quit the game so we break the while look
		elif choice == '3':
			break

	#	The only way the player end up here is if the dies or quit so lets check and give them one more last message
	#	If they still have hp then they quit the game
	if player["hp"] > 0:
		print("You retire and live a heppy life.")
	else:
		print("You died!")
	
	