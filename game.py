def main():
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    player_choice = get_user_input()#this holds the choice in this function
    second_choice = get_random_choice(gesture_list)# this holds the choice in this function
    determine_winner(player_choice, second_choice, gesture_list)# determine winner function



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


def determine_winner(player_choice, second_choice, gesture_list):
    
    if player_choice == "1":
        if second_choice == (gesture_list[1]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[1]))
            print("Paper covers Rock!")
            print("")
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
        elif second_choice == (gesture_list[0]):
            print("You choose Rock.")
            print("AI chooses:",(gesture_list[0]))
            print("TIE. Go again.")
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
         

         pass

main()










        




        


        


        


        
    

































  








