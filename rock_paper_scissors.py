import random # Needed for random selection

def userChoice():
    '''Function gets user input for the game'''
    # User input
    choice = input("Type 'r' for rock, 'p' for paper or 's' for scissors: ")
    return choice # Variable must be returned to be stored
    
def compChoice():
    '''Function defines computer behaviour for the game'''
    choices = ['r', 'p', 's'] # List for computer to choose from
    com = random.choice(choices)
    word = com

    match word: # Turns computer choice into a word
        case "r":
            word = "rock"
        case "p":
            word = "paper"
        case "s":
            word = "scissors"
    
    print(f"The computer chose {word}.")
    return com
    
def winner(usr, com):
    '''Function compares user and computer input to find a winner'''
    if usr == com:
        print("It's a tie!")
    elif (usr == 'r' and com == 's') or (usr == 's' and com == 'p') or (usr == 'p' and com == 'r'):
        print("You won!")
    else:
        print("You lost!")
    
print("** Rock Paper Scissors **")

yn = ""
while (yn.lower() != "n"):
    usr_choice = userChoice()
    com_choice = compChoice()
    winner(usr_choice, com_choice)
    yn = input("Would you like to continue? y/n: ")
