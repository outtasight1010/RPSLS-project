import random

class Gestures:
    def __init__(self):
        self.list = ["Rock","Paper","Scissors","Lizard","Spock"] 
           
        pass
    import random

    def get_gesture(self):
        gesture = random.choice(self.list)
        return gesture
    
    def user_choice(self):
        player_choice = input("Please choose a gesture(type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
        while player_choice!="1" and player_choice!="2" and player_choice!= "3" and player_choice!="4" and player_choice!="5":
            print("Oops, you must choose a number listed. Please try again.")
            player_choice = input("Please choose a gesture(type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
            
        else:
            if player_choice == "1" and random.choice(gesture.list) == (gesture.list[0]):
                print("You choose Rock.")
                print("AI chooses:",(gesture.list[0]))
                print("TIE.Go again.")
                player_choice = input("Please choose a gesture(type corresponding number): \n1 for Rock.\n2 for Paper.\n3 for Scissors.\n4 for Lizard.\n5 for Spock. ")
            if player_choice == "1" and random.choice(gesture.list) == (gesture.list[3]):
                print("You choose Rock.")
                print("AI chooses:",(gesture.list[3]))
                print("Rock crushes Lizard!")
            if player_choice == "1" and random.choice(gesture.list) == (gesture.list[1]):
                print("You choose Rock.")
                print("AI chooses:",(gesture.list[1]))
                print("Paper covers Rock!")
            if player_choice == "1" and random.choice(gesture.list) == (gesture.list[2]):
                print("You choose Rock.")
                print("AI chooses:",(gesture.list[2]))
                print("Rock crushes Scissors!")
            if player_choice == "1" and random.choice(gesture.list) == (gesture.list[4]):
                print("You choose Rock.")
                print("AI chooses:",(gesture.list[4]))
                print("Spock vaporizes Rock!")
            
            elif player_choice == "2" and random.choice(gesture.list) == (gesture.list[0]):
                print("You choose Paper.")
                print("AI chooses:",(gesture.list[0]))
                print("Paper covers Rock!")
            elif player_choice == "2" and random.choice(gesture.list) == (gesture.list[2]):
                print("You choose Paper.")
                print("AI chooses:",(gesture.list[2]))
                print("Scissors cuts Paper!")



                
                    
        
             
gesture = Gestures()
#print("AI chooses:",random.choice(gesture.list))
#gesture.get_gesture() #used to retrieve random gesture
gesture.user_choice()









    







        