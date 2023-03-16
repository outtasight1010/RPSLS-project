def main():



    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]

def get_user_input():# create function to get user(player 1) input
    
    player_choice = input("Player, please choose a gesture (type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    while player_choice!="1" and player_choice!="2" and player_choice!= "3" and player_choice!="4" and player_choice!="5":
        print("Oops, you must choose a number listed. Please try again.")
        player_choice = input("Please choose a gesture(type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
    else:
        return player_choice
    
player_choice = get_user_input

def get_random_choice():# create function to retrieve random gesture
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    import random
    
    second_choice = random.choice(gesture_list)
    return second_choice

second_choice = get_random_choice

def determine_winner():
    player_choice = get_user_input
    
    second_choice = get_random_choice

    import random
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    second_choice = random.choice(gesture_list)
    if player_choice == "1":
        if second_choice == random.choice(gesture_list[1]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[1]))
            print("Paper covers Rock!")
            print("")
    if player_choice == "1":
        if second_choice == random.choice(gesture_list[2]): 
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[2]))
            print("Rock crushes Scissors!")


get_user_input()
get_random_choice()
determine_winner()






























  








