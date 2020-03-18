from random import randint #for the computer opponent to be able to play

t = ["Rock", "Paper", "Scissors"]#create a list of play options

computer = t[randint(0,2)]#assign a random play to the computer

player = False #set player to False

while player == False:#sets the player to True
    player = input("Rock, Paper, Scissors?")#the player inputs the turn
    if player == computer:
        print("Tie!") #if both the computer and the player has made the same turn
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")#The program is case sensitive so if a player has

    player = False#the player will be seat to false for the loop to restart  and continue the game
    computer = t[randint(0,2)]#assign a random play to the computer