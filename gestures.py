import random

class Gestures:
    def __init__(self):
        self.list = ["Rock","Paper","Scissors","Lizard","Spock"] 
           
        pass
    import random

    def get_gesture(self):
        gesture = random.choice(self.list)
        return gesture
    


gesture = Gestures()
print("AI chooses:",random.choice(gesture.list))
gesture.get_gesture()










    







        