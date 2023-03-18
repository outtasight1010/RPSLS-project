
def main():
    first_player = 0 #created a counter for player 1
    second_player = 0 #created a counter for player 2
    game_times = 0 #created a counter for each time they draw a gesture, in this case we want best out of three
    
    choice_of_game = game_choice() #allows user to choose option 1.One player game, or 2.Two player game
    
    player_1_choice = player_1_input() #variable created for Player One
    player_2_choice = player_2_input() #variable created for Player Two
    winner_game_2(player_1_choice, player_2_choice) # created to determine gesture choices

    


def game_choice_2(first_player, second_player, game_times): #determine whether user wants to play 1 or 2 player game
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    player_1_choice = player_1_input()#this holds the choice in this function
    player_2_choice = player_2_input(gesture_list)# this holds the choice in this function
    winner_game_2(player_1_choice, player_2_choice, gesture_list, first_player, second_player, game_times)# determine winner function





def open_greeting():
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock! Or what we'd like to call RPSLS!")
        print("")
        print("Ok, listen up. Here are the rules of the game: \n1.Rock crushes Scissors.\n2.Scissor cuts Paper.\n3.Paper covers Rock.\n4.Rock crushes Lizard."
              "\n5.Paper disproves Spock. \n6.Spock vaporizes Rock. \n7.Lizard poisons Spock. \n8.Spock smashes Scissors. \n9.Scissors decapitates Lizard.\n10.Lizard eats Paper.")
        print("")
        print("We will go BEST out of THREE. May the best player WIN. Let's begin:")
        print("")    





def game_choice():
    choice_of_game = input("Hi, please type 1. for One Player Game, or 2. for Two Player Game.")
    while choice_of_game != "1" and choice_of_game != "2":
        print("Oopsie, you must type in 1 or 2. Be go again.")
        choice_of_game = input("Hi, please type 1. for One Player Game, or 2. for Two Player Game.")
    else:
        if choice_of_game == "1":
            print("You have chosen: One Player Game.")
        elif choice_of_game == "2":
            print("You have chosen: Two Player Game.")
        return choice_of_game



def player_1_input():# create function to get user(player 1) input
    player_1_choice = input("Player One, please choose a gesture (type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    while player_1_choice!="1" and player_1_choice!="2" and player_1_choice!= "3" and player_1_choice!="4" and player_1_choice!="5":
        print("Oops, you must choose a number listed. Please try again.")
        player_1_choice = input("Player One, please choose a gesture (type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    else:
        return player_1_choice
    

def player_2_input():# create function to get user(player 1) input
    player_2_choice = input("Player Two, please choose a gesture (type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    while player_2_choice!="1" and player_2_choice!="2" and player_2_choice!= "3" and player_2_choice!="4" and player_2_choice!="5":
        print("Oops, you must choose a number listed. Please try again.")
        player_2_choice = input("Player Two, please choose a gesture (type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    else:
        return player_2_choice
    

def winner_game_2(player_1_choice, player_2_choice):
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    
    if player_1_choice == (gesture_list[0]):
        if player_2_choice == (gesture_list[0]):
            print("Player One chooses:",(gesture_list[0]))
            print("Player Two chooses:",(gesture_list[0]))
            print("TIE. Go again.")
            print("")
        elif player_2_choice == (gesture_list[1]):
           print("Player One chooses:",(gesture_list[0]))
           print("Player Two chooses:",(gesture_list[1]))
           print("Paper covers Rock!")
           print("")
        elif player_2_choice == (gesture_list[2]):
           print("Player One chooses:",(gesture_list[0]))
           print("Player Two chooses:",(gesture_list[2]))
           print("Rock crushes Scissors!")
           print("")
        elif player_2_choice == (gesture_list[3]):
           print("Player One chooses:",(gesture_list[0]))
           print("Player Two chooses:",(gesture_list[3]))
           print("Rock crushes Lizard!")
           print("")
        elif player_2_choice == (gesture_list[4]):
           print("Player One chooses:",(gesture_list[0]))
           print("Player Two chooses:",(gesture_list[4]))
           print("Spock vaporizes Rock!")
           print("")
    elif player_1_choice == (gesture_list[1]):
        if player_2_choice == (gesture_list[0]):
           print("Player One chooses:",(gesture_list[1]))
           print("Player Two chooses:",(gesture_list[0]))
           print("Paper covers Rock!")
           print("")
           #continue Mish from here
        elif player_2_choice == (gesture_list[1]):
           print("Player One chooses:",(gesture_list[1]))
           print("Player Two chooses:",(gesture_list[1]))
           print("TIE. Go again.")
           print("")
        elif player_2_choice == (gesture_list[2]):
           print("Player One chooses:",(gesture_list[1]))
           print("Player Two chooses:",(gesture_list[2]))
           print("Scissors cuts Paper!")
           print("")
        elif player_2_choice == (gesture_list[3]):
           print("Player One chooses:",(gesture_list[1]))
           print("Player Two chooses:",(gesture_list[3]))
           print("Lizard eats Paper!")
           print("")
        elif player_2_choice == (gesture_list[4]):
           print("Player One chooses:",(gesture_list[1]))
           print("Player Two chooses:",(gesture_list[4]))
           print("Paper disproves Spock!")
           print("")
    elif player_1_choice == (gesture_list[2]):        
        if player_2_choice == (gesture_list[0]):
           print("Player One chooses:",(gesture_list[2]))
           print("Player Two chooses:",(gesture_list[0]))
           print("Rock crushes Scissors!")
           print("")
        elif player_2_choice == (gesture_list[1]):
           print("Player One chooses:",(gesture_list[2]))
           print("Player Two chooses:",(gesture_list[1]))
           print("Scissors cuts Paper!")
           print("")
        elif player_2_choice == (gesture_list[2]):
           print("Player One chooses:",(gesture_list[2]))
           print("Player Two chooses:",(gesture_list[2]))
           print("TIE. Go again.")
           print("")
        elif player_2_choice == (gesture_list[3]):
           print("Player One chooses:",(gesture_list[2]))
           print("Player Two chooses:",(gesture_list[3]))
           print("Scissors decapitates Lizard!")
           print("")
        elif player_2_choice == (gesture_list[4]):
           print("Player One chooses:",(gesture_list[2]))
           print("Player Two chooses:",(gesture_list[4]))
           print("Spock smashes Scissors!")
           print("")
    elif player_1_choice == (gesture_list[3]):
        if player_2_choice == (gesture_list[0]):
           print("Player One chooses:",(gesture_list[3]))
           print("Player Two chooses:",(gesture_list[0]))
           print("Rock crushes Lizard!")
           print("")
        elif player_2_choice == (gesture_list[1]):
           print("Player One chooses:",(gesture_list[3]))
           print("Player Two chooses:",(gesture_list[1]))
           print("Lizard eats Paper!")
           print("")
        elif player_2_choice == (gesture_list[2]):
           print("Player One chooses:",(gesture_list[3]))
           print("Player Two chooses:",(gesture_list[2]))
           print("Scissors decapitates Lizard!")
           print("")
        elif player_2_choice == (gesture_list[3]):
           print("Player One chooses:",(gesture_list[3]))
           print("Player Two chooses:",(gesture_list[3]))
           print("TIE. Go again.")
           print("")
        elif player_2_choice == (gesture_list[4]):
           print("Player One chooses:",(gesture_list[3]))
           print("Player Two chooses:",(gesture_list[4]))
           print("Lizard poisons Spock!")
           print("")
    elif player_1_choice == (gesture_list[4]):  
        if player_2_choice == (gesture_list[0]):
           print("Player One chooses:",(gesture_list[4]))
           print("Player Two chooses:",(gesture_list[0]))
           print("Spock vaporizes Rock!")
           print("")
        elif player_2_choice == (gesture_list[1]):
           print("Player One chooses:",(gesture_list[4]))
           print("Player Two chooses:",(gesture_list[1]))
           print("Paper disproves Spock!")
           print("")
        elif player_2_choice == (gesture_list[2]):
           print("Player One chooses:",(gesture_list[4]))
           print("Player Two chooses:",(gesture_list[2]))
           print("Spock smashes Scissors!")
           print("")
        elif player_2_choice == (gesture_list[3]):
           print("Player One chooses:",(gesture_list[4]))
           print("Player Two chooses:",(gesture_list[3]))
           print("Lizard poisons Spock!")
           print("")
        elif player_2_choice == (gesture_list[4]):
           print("Player One chooses:",(gesture_list[4]))
           print("Player Two chooses:",(gesture_list[4]))
           print("TIE. Go again.")


player_1_input()
player_2_input()




