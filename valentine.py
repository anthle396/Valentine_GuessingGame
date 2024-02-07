###########################################################################
#                          MAIN PROGRAM FILE                              
#			     valetine.py 								  
###########################################################################
# Functionality: This program will act as a guessing game				  
# that will ask the user to guess what the word is but really it This	  
# asking the user to be my valentine                     				  
# Contributors: Anthony Le							                      
# Date Created: 02/06/2024                                                
# Last Updated: 02/06/2024 Anthony                                  	  
###########################################################################

################### Functions #######################

#########################################################################################################
# @function clear() 			- Displays a ton of newlines (\n) so that it looks like page is cleared
# @return none
#########################################################################################################
# Clear function takes in nothing and makes a lot of newliens
def clear():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#########################################################################################################
# @function display_guess() 		- Takes the letter_dict and decodes the values that have been enabled
#					  by a 1 and if not then returns an '_' back to the output
# @param letter_dict 			- A dictionary that stores all the possible values to be guessed 
#					  and sets their value as 1 when guessed
#
# @return output			- returns a string of the guessed and unguessed letters
#########################################################################################################
# Function that displays a letter for every one guessed
def display_guess(letter_dict):
    # The word to be guessed
    word = "WILL YOU BE MY VALENTINE"
    # Initialize an empty string to store the output
    output = ""
    # Iterate through each character in the word
    for i, letter in enumerate(word):
        # If the character is a space, add a space to the output
        if letter == " ":
            output += " "
        # If the letter has been guessed (its value in letter_dict is 1), add the uppercase letter to the output
        elif letter_dict.get(letter.lower(), 0) == 1:
            output += letter.upper() + " "
        # If the letter has not been guessed, add an underscore to the output
        else:
            output += "_ "
    # Return the output string
    return output

#########################################################################################################
# @function handle_guess() 		- Handles each letter case and changes letter_dict and returns it back
# @param guess 				- A char that is the letter the user guessed 
# @param letter_dict 			- A dictionary that stores all the possible values to be guessed 
#					  and sets their value as 1 when guessed
# @param max_len			- The max_len of letters the user can guess
#
# @return letter_dict, max_len		- Returns the letter_dict back and the max_len of the words remaining
#########################################################################################################
def handle_guess(guess, letter_dict, max_len):
    # Clear the screen or perform any necessary clearing operation
    clear()

    # Define the list of valid guesses
    valid_guesses = ['l', 'w', 'i', 'y', 'o', 'u', 'b', 'e', 'm', 'v', 'a', 'n', 't']

    # Check if the guess is a valid guess and if the letter has not been guessed before
    if guess.lower() in valid_guesses and letter_dict.get(guess.lower(), 0) != 1:
        # If the guess is valid and the letter has not been guessed before, update letter_dict and decrement max_len
        letter_dict[guess.lower()] = 1
        max_len -= 1
        return letter_dict, max_len

    # If the guess is not valid or the letter has already been guessed, inform the user and return the unchanged letter_dict and max_len
    print("You already guessed this letter silly! Try again.")
    print("--------------------------------------------\n\n")
    return letter_dict, max_len


################### Mainline ########################
if __name__ == "__main__":
	
	# Vars
	hearts = 3
	string = "willyoubemyvalentine"

	# Create a set of unique characters in the string
	unique_chars = set(string)

	# Create a dictionary with default values of 0 for each unique character
	letter_dict = {char: 0 for char in unique_chars}
	max_len = 13

	# print(letter_dict) # for debugging

	# Welcomes the user to the program!
	print("Hello and welcome to the guessing game!!")
	print("--------------------------------------------")

	# Prompts user to enter their name
	name = input ("Please enter your name: ")

	# Checks to see if the user entered the correct name
	while (1):
		choice = input("Your name is " + name + ". Is this correct (y/n): ")
		# If player doens't want to play exits
		if (choice.lower() == "n"):
			clear()
			name = input ("Please re-enter your name: ")
		
		# If player renames
		elif (choice.lower() == "y"):
			clear()
			break;

		# If player enters an invalid input
		else:	
			clear()
			print("Not a valid input. Try again dummy.\n")
			choice = input("Your name is " + name + ". Is this correct (y/n): ")

	# Prompts user to play game and checks answer
	choice = input("Hello "+ str(name) + "! Would you like to play? (y/n): ").lower()

	while (1):
		# If player doens't want to play exits
		if (choice.lower() == "n"):
			clear()
			print("Exiting game...\n")
			exit(1)
		
		# If player wants to play exits loop
		elif (choice.lower() == "y"):
			clear()
			break;

		# If player enters an invalid input
		else:	
			clear()
			print("Not a valid input. Try again dummy.\n")
			choice = input("Would you like to play? (y/n): ").lower()

	# Creates a lot of newlines
	print("Welcome to the game!\nPlease enter a word to guess!\n")
	print("You currently have " + str(hearts) +" \u2665. The word is:\n")
	print("_ _ _ _   _ _ _   _ _   _ _   _ _ _ _ _ _ _ _ _\n\n")

	# Var for guess
	guess = ""

	# Loop for guessing
	while (max_len != 0):
		# Prompts user to guess a letter
		guess = input("Please enter a letter to guess: ").lower()

		# If guess is correct fills out the blank space
		# and decr max_len until all are guessed
		# or out of lives
		if guess in string:
			(letter_dict, max_len) = handle_guess(guess, letter_dict, max_len)
		
		# If not in guess subtract life
		elif guess not in string:
			clear()
			print("Incorrect! - \u2665 Heart")
			hearts -= 1

			# If no lives left game over
			if hearts == 0:
				clear()
				print("Game Over :(\nNot only did you lose but you suck\n\n\n\n")
				print("--------------------------------------------")
				print("Exiting...\n\n\n\n\n")
				exit(1)
		
		# if all numbers have been guessed exit out of loop
		if max_len == 0:
			break;

		# Displays current results
		print("You currently have " + str(hearts) +" \u2665. The word is:\n")
		# print(letter_dict) # for debugging dictionary
		# print("max_len = ",max_len) # for debugging max_len
		print("\n")
		print(display_guess(letter_dict))

	# Once you win the game displays victory message
	print("The word is:")
	print("--------------------------------------------")
	print(display_guess(letter_dict) + "?")
	print("--------------------------------------------\n\n")
	print("\u2665\u2665 CONGRATULATIONS \u2665\u2665 YOU HAVE WON THE GAME \u2665\u2665!!!!!!\n")
	print("AND YOU HAVE ALSO WON MY HEART \u2665\u2665\u2665!!!!!!\n")
	# Prompts user to enter y/n and checks answer
	choice = input(str(name) + ", WILL YOU BE MY VALENTINE \u2665? (y/n): ").lower()

	# var for valentine loop display
	i = 0
	# Checks to see if the user entered the correct name
	while (1):
		# If player doens't want to play exits
		if (choice.lower() == "n"):
			clear()
			choice = input ("Are you sure you said no and not yes (ㆆ _ ㆆ)? (y/n): ")
			
			if (choice.lower() == "y"):
				clear()
				print("Nah try again.")
				choice = input(str(name) + ", WILL YOU BE MY VALENTINE \u2665? (y/n): ").lower()
			
			elif(choice.lower() == "n"):
				print("Hmmm lets try again... (ㆆ ____ㆆ)")
				choice = input(str(name) + ", WILL YOU BE MY VALENTINE \u2665? (y/y): ").lower()
				
				if (choice.lower() == "y"):
					print("\n\nHOORAYYYYYYYYYYYYYYYYYY YAYYYYYYYYYYYYYY \u2665\u2665\u2665!!!!\n\n")
					
					while i < 24:
						print("\u2665 HAPPY VALENTINESS \u2665 " + str(name) + "!!!!!!!!!")
						i += 1
					exit(1)
				
				else:
					clear()
					print("Not a valid input. Try again dummy.\n")
					choice = input(str(name) + ", WILL YOU BE MY VALENTINE \u2665? (y/y): ").lower()

		# If player renames
		elif (choice.lower() == "y"):
			clear()
			print("HOORAYYYYYYYYYYYYYYYYYY YAYYYYYYYYYYYYYY \u2665\u2665\u2665!!!!\n\n")
			while i < 24:
				print("\u2665 HAPPY VALENTINESS \u2665 " + str(name) + "!!!!!!!!!")
				i += 1
			exit(1)
		# If player enters an invalid input
		else:	
			clear()
			print("Not a valid input. Try again dummy.\n")
			choice = input(str(name) + ", WILL YOU BE MY VALENTINE \u2665? (y/n): ").lower()




