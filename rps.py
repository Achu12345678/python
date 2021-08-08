# Made by Achu#9225 on discord
# Rock Paper Scissors Multi-Round Game
# You can use with credit :)
# 8/8/2021



import random
import time


global comp_wins
global player_wins

game_map = {0:"rock", 1:"paper", 2:"scissors"}


name = input("Enter your name: ")

def play_again():

    play_again_question = input("Would you like to play again? (yes/no)")
            
    if play_again_question.lower() == "yes":
        rps_round_select()
    elif play_again_question.lower() == "no":
        quit_confirmation()
    else:
        print("Please submit a valid answer and try again.")
        play_again()
                
                
def rps_instructions():

    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()


def rps_3round_game():

    player_wins = 0
    comp_wins = 0

    while True:

        if player_wins == 3:
            print(name, "has won the game! Well done!")
            play_again()
        elif comp_wins == 3:
            print("The computer has the game! Better luck next time. :(")    
            play_again()
        elif player_wins < 3 or comp_wins < 3:


            print("--------------------------------------")
            print("Three Round Game")
            print("--------------------------------------")
            print("Player Wins: ", player_wins)
            print()
            print("Computer Wins: ", comp_wins)
            print("Enter \"Rock\",\"Paper\",\"Scissors\" to start/continue")
            print("--------------------------------------")
            
            print()
                
            inp = input("Enter your move: ")

            if inp.lower() == "rock":
                player_move = 0
            elif inp.lower() == "paper":
                player_move = 1
            elif inp.lower() == "scissors":
                player_move = 2
            else:
                print("Wrong Input!")
                rps_instructions()
                time.sleep(4)
                continue
                
            print("Computer is making a move...")

            print()
            time.sleep(2)

            comp_move = random.randint(0, 2)

            print("Computer chooses:", game_map[comp_move].upper())

            if player_move == comp_move:
                print(name, "and the computer have both chosen the same move! It's a tie!")
                continue
            elif (player_move == 0 and comp_move == 2) or (player_move == 2 and comp_move == 1) or (player_move == 1 and comp_move == 0):
                player_wins += 1
                print(name, "has won this round! Good job!")
                continue
            else:
                comp_wins += 1
                print("The computer has won this round!")
                continue


def rps_5round_game():

    player_wins = 0
    comp_wins = 0

    while True:

        if player_wins == 5:
            print(name, "has won the game! Well done!")
            play_again()
        elif comp_wins == 5:
            print("The computer has the game! Better luck next time. :(")    
            play_again()
        elif player_wins < 5 or comp_wins < 5:


            print("--------------------------------------")
            print("Five Round Game")
            print("--------------------------------------")
            print("Player Wins: ", player_wins)
            print()
            print("Computer Wins: ", comp_wins)
            print("Enter \"Rock\",\"Paper\",\"Scissors\" to start/continue")
            print("--------------------------------------")
            
            print()
                
            inp = input("Enter your move: ")

            if inp.lower() == "rock":
                player_move = 0
            elif inp.lower() == "paper":
                player_move = 1
            elif inp.lower() == "scissors":
                player_move = 2
            else:
                print("Wrong Input!")
                rps_instructions()
                time.sleep(4)
                continue
                
            print("Computer is making a move...")

            print()
            time.sleep(2)

            comp_move = random.randint(0, 2)

            print("Computer chooses:", game_map[comp_move].upper())

            if player_move == comp_move:
                print(name, "and the computer have both chosen the same move! It's a tie!")
                continue
            elif (player_move == 0 and comp_move == 2) or (player_move == 2 and comp_move == 1) or (player_move == 1 and comp_move == 0):
                player_wins += 1
                print(name, "has won this round! Good job!")
                continue
            else:
                comp_wins += 1
                print("The computer has won this round!")
                continue


def rps_10round_game():

    player_wins = 0
    comp_wins = 0

    while True:

        if player_wins == 10:
            print(name, "has won the game! Well done!")
            play_again()
        elif comp_wins == 10:
            print("The computer has the game! Better luck next time. :(")    
            play_again()
        elif player_wins < 10 or comp_wins < 10:


            print("--------------------------------------")
            print("Ten Round Game")
            print("--------------------------------------")
            print("Player Wins: ", player_wins)
            print()
            print("Computer Wins: ", comp_wins)
            print("Enter \"Rock\",\"Paper\",\"Scissors\" to start/continue")
            print("--------------------------------------")
            
            print()
                
            inp = input("Enter your move: ")

            if inp.lower() == "rock":
                player_move = 0
            elif inp.lower() == "paper":
                player_move = 1
            elif inp.lower() == "scissors":
                player_move = 2
            else:
                print("Wrong Input!")
                rps_instructions()
                time.sleep(4)
                continue
                
            print("Computer is making a move...")

            print()
            time.sleep(2)

            comp_move = random.randint(0, 2)

            print("Computer chooses:", game_map[comp_move].upper())

            if player_move == comp_move:
                print(name, "and the computer have both chosen the same move! It's a tie!")
                continue
            elif (player_move == 0 and comp_move == 2) or (player_move == 2 and comp_move == 1) or (player_move == 1 and comp_move == 0):
                player_wins += 1
                print(name, "has won this round! Good job!")
                continue
            else:
                comp_wins += 1
                print("The computer has won this round!")
                continue





def rps_round_select():

    while True:
    
        global player_wins
        player_wins = 0
        

        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"3\" for a first to 3 round game")
        print("Enter \"5\" for a first to 5 round game")
        print("Enter \"10\" for a first to 10 round game")
        print("--------------------------------------")
        
        global roundselect

        roundselect = input("Enter your round number: ")

        if roundselect == '3':
            rps_3round_game()
        elif roundselect == '5':
            rps_5round_game()
        elif roundselect == '10':
            rps_10round_game()
        else:
            print("Please submit a valid answer and try again.")
            continue



def quit_confirmation():

    while True:
        
        quit_confirm = input("""
        -------------------------------------
        Are you sure you want to quit? (yes/no)
        -------------------------------------
        """)

        if quit_confirm == "yes":
            exit()
        elif quit_confirm == "no":
            rps_round_select()
        else:
            print("Please submit a valid answer and try again.")
            continue

player_wins = 0
comp_wins = 0



while True:
    print()
    print("Let's Play!!!")
    print("Enter 1 to play Rock-Paper-Scissors")
    print("Enter 2 to quit")
    print()
            
    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        print("Wrong Choice")
        continue


    if choice == 1:
        rps_round_select()
    elif choice == 2:
        quit_confirmation()
    else:
        print("Error, please enter a valid number and try again.")
