import random
import os

#Define main game function
def game():
    os.system('cls')
    #Create list of random words, run random module to choose a random word out of the list
    wordlist = 'apple dog phone gamer gunk alphabet remorse guitar desert fish farzar'.split()
    secretWord = random.choice(wordlist)

    #Define the ammount of turns that the user will have
    turns = 10

    #Variable to store all letters that the user has guessed
    guesses = ''

    #Start main loop
    while turns > 0:
        failed = 0 #This fail counter is used decide whether the user has won the game
        for char in secretWord:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1

        if failed == 0:
            os.system('cls')
            print('YOU WIN!')
            retry = input("Try again? (Y/N)")
            if retry == 'Y':
                game()
            else:
                exit()
        #Ask user to enter a character, then add the "guess" into the "guesses variable"
        guess = input("Enter a character: ")
        guesses += guess

        if guess not in secretWord:
            print("Wrong, you have " + str(turns) + ' turns left')
            turns -= 1
        if turns == 0:
            lostGame()

 #Define the function that runs when the user loses the game by using up all their turns.       
def lostGame():
    os.system('cls')
    print("\nLOSER!")
    retry = input("Retry? (Y/N): ")
    if retry == 'Y':
        game()
    else:
        print("Fine, loser..")
        exit()


#Running the game 
game()

