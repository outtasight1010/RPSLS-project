class Greeting:
    def __init__(self):
        pass 
    #creating greeting for game

    def open_greeting(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock! Or what we'd like to call RPSLS!")
        print("")

    def games_rules(self):
        print("")
        print("Ok, listen up. Here are the rules of the game: \n1.Rock crushes Scissors.\n2.Scissor cuts Paper.\n3.Paper covers Rock.\n4.Rock crushes Lizard."
              "\n5.Paper disproves Spock. \n6.Spock vaporizes Rock. \n7.Lizard poisons Spock. \n8.Spock smashes Scissors. \n9.Scissors decapitates Lizard.\n10.Lizard eats Paper.")
        print("")
        print("We will go BEST out of THREE. May the best player WIN. Let's begin:")
        print("")


games = Greeting()

games.open_greeting()
games.games_rules()



