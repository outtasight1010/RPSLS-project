def main():
    first_player = 0
    computer_player = 0
    game_times = 0
    open_greeting()
    choice_of_game = game_choice()
    if choice_of_game == "1":
        game_choice_1(first_player, computer_player, game_times)
    elif choice_of_game == "2":
        print("not wready pwease")
    

def game_choice_1(first_player, computer_player, game_times):
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    player_choice = get_user_input()#this holds the choice in this function
    second_choice = get_random_choice(gesture_list)# this holds the choice in this function
    determine_winner(player_choice, second_choice, gesture_list, first_player, computer_player, game_times)# determine winner function




def open_greeting():
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock! Or what we'd like to call RPSLS!")
        print("")
        print("Ok, listen up. Here are the rules of the game: \n1.Rock crushes Scissors.\n2.Scissor cuts Paper.\n3.Paper covers Rock.\n4.Rock crushes Lizard."
              "\n5.Paper disproves Spock. \n6.Spock vaporizes Rock. \n7.Lizard poisons Spock. \n8.Spock smashes Scissors. \n9.Scissors decapitates Lizard.\n10.Lizard eats Paper.")
        print("")
        print("We will go BEST out of THREE. May the best player WIN. Let's begin:")
        print("")

def get_user_input():# create function to get user(player 1) input
    player_choice = input("Player, please choose a gesture (type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    while player_choice!="1" and player_choice!="2" and player_choice!= "3" and player_choice!="4" and player_choice!="5":
        print("Oops, you must choose a number listed. Please try again.")
        player_choice = input("Please choose a gesture(type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    else:
        return player_choice
    

def get_random_choice(gesture_list):# create function to retrieve random gesture
    import random
    second_choice = random.choice(gesture_list)
    return second_choice


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


    
def determine_winner(player_choice, second_choice, gesture_list, first_player, computer_player, game_times):

    if player_choice == "1":
        if second_choice == (gesture_list[0]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[0]))
            print("TIE. Go again.")
            game_choice_1(first_player, computer_player, game_times)
        elif second_choice == (gesture_list[1]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[1]))
            print("Paper covers Rock!")
            print("")
            computer_player += 1
            game_times += 1
            if game_times < 3:
                game_choice_1(first_player, computer_player, game_times)
            else:
                print("game over pwease")

        elif second_choice == (gesture_list[2]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[2]))
            print("Rock crushes Scissors!")
            print("")
        elif second_choice == (gesture_list[3]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[3]))
            print("Rock crushes Lizard!")
            print("")
        elif second_choice == (gesture_list[4]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[4]))
            print("Spock vaporizes Rock!")
            print("")
        
    elif player_choice == "2":
        if second_choice == (gesture_list[0]):
            print("You choose Paper.")
            print("AI chooses:",(gesture_list[0]))
            print("Paper covers Rock!")
            print("")
        elif second_choice == (gesture_list[1]):
            print("You choose Paper.")
            print("AI chooses:",(gesture_list[1]))
            print("TIE. Go again.")
        elif second_choice == (gesture_list[2]):
            print("You choose Paper.")
            print("AI chooses:",(gesture_list[2]))
            print("Scissors cuts Paper!")
            print("")
        elif second_choice == (gesture_list[3]):
            print("You choose Paper.")
            print("AI chooses:",(gesture_list[3]))
            print("Lizard eats Paper!")
            print("")
        elif second_choice == (gesture_list[4]):
            print("You choose Paper.")
            print("AI chooses:",(gesture_list[4]))
            print("Paper disproves Spock!")
            print("")
    elif player_choice == "3":        
        if second_choice == (gesture_list[0]):
            print("You choose Scissors.")
            print("AI chooses:",(gesture_list[0]))
            print("Rock crushes Scissors!")
            print("")
        elif second_choice == (gesture_list[1]):
            print("You choose Scissors.")
            print("AI chooses:",(gesture_list[1]))
            print("Scissors cuts Paper!")
            print("")
        elif second_choice == (gesture_list[2]):
            print("You choose Scissors.")
            print("AI chooses:",(gesture_list[2]))
            print("TIE. Go again.")
            print("")
        elif second_choice == (gesture_list[3]):
            print("You choose Scissors.")
            print("AI chooses:",(gesture_list[3]))
            print("Scissors decapitates Lizard!")
            print("")
        elif second_choice == (gesture_list[4]):
            print("You choose Scissors.")
            print("AI chooses:",(gesture_list[4]))
            print("Spock smashes Scissors!")
            print("")
    elif player_choice == "4":
        if second_choice == (gesture_list[0]):
            print("You choose Lizard.")
            print("AI chooses:",(gesture_list[0]))
            print("Rock crushes Lizard!")
            print("")
        elif second_choice == (gesture_list[1]):
            print("You choose Lizard.")
            print("AI chooses:",(gesture_list[1]))
            print("Lizard eats Paper!")
            print("")
        elif second_choice == (gesture_list[2]):
            print("You choose Lizard.")
            print("AI chooses:",(gesture_list[2]))
            print("Scissors decapitates Lizard!")
            print("")
        elif second_choice == (gesture_list[3]):
            print("You choose Scissors.")
            print("AI chooses:",(gesture_list[3]))
            print("TIE. Go again.")
            print("")
        elif second_choice == (gesture_list[4]):
            print("You choose Lizard.")
            print("AI chooses:",(gesture_list[4]))
            print("Lizard poisons Spock!")
    elif player_choice == "5":  
        if second_choice == (gesture_list[0]):
            print("You choose Spock.")
            print("AI chooses:",(gesture_list[0]))
            print("Spock vaporizes Rock!")
            print("")
        elif second_choice == (gesture_list[1]):
            print("You choose Spock.")
            print("AI chooses:",(gesture_list[1]))
            print("Paper disproves Spock!")
            print("")
        elif second_choice == (gesture_list[2]):
            print("You choose Spock.")
            print("AI chooses:",(gesture_list[2]))
            print("Spock smashes Scissors!")
            print("")
        elif second_choice == (gesture_list[3]):
            print("You choose Spock.")
            print("AI chooses:",(gesture_list[3]))
            print("Lizard poisons Spock!")
            print("")
        elif second_choice == (gesture_list[4]):
            print("You choose Spock.")
            print("AI chooses:",(gesture_list[4]))
            print("TIE. Go again.")

main()










    
        
            
        
        
        

        
    










        




        


        


        


        
    

































  








