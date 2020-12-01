import random

class WrongChoiceError(Exception):
    """ Raise this error if the user enters wrong choice"""
    pass

def choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors.\n******Rules******\nYou can either enter the entire word i.e. rock,paper,scissors or just their initials i.e. r for rock and so on:\nLet's begin playing this game")
    while True:
        _choice = choice()
        print("It's your turn.\nPlease enter your choice:")
        try:
            player_choice = input()
            if any([player_choice == "rock", player_choice == "r", player_choice == "paper", player_choice.lower() == "p", player_choice == "scissors", player_choice == "s"]):
                if (player_choice.lower() == "rock" or player_choice.lower() == "r") and (_choice == "scissors" ):
                    print("You won !")
                elif (player_choice.lower() == "rock" or player_choice.lower() == "r") and (_choice == "paper" ):
                    print("You lost !")
                elif (player_choice.lower() == "scissors" or player_choice.lower() == "s") and (_choice == "paper" ):
                    print("You won !")
                elif (player_choice.lower() == "scissors" or player_choice.lower() == "s") and (_choice == "rock" ):
                    print("You lost !")
                elif (player_choice.lower() == "paper" or player_choice.lower() == "p") and (_choice == "rock" ):
                    print("You won !")
                elif (player_choice.lower() == "paper" or player_choice.lower() == "p") and (_choice == "scissors" ):
                    print("You lost !")
                elif (player_choice.lower() == "paper" or player_choice.lower() == "p") and (_choice == "paper" ):
                    print("It's a tie !")
                    continue
                elif (player_choice.lower() == "scissors" or player_choice.lower() == "s") and (_choice == "scissors" ):
                    print("It's a tie !")
                    continue
                elif (player_choice.lower() == "rock" or player_choice.lower() == "r") and (_choice == "rock" ):
                    print("It's a tie !")
                    continue
            else:
                raise WrongChoiceError
                
        except WrongChoiceError:
            print("Please enter a valid choice !")
        

rock_paper_scissors()