import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Name_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Name_Card_Game_Score.txt", "w") as document:
        if (wins >= 1000000000):
            document.write(str(wins))
        elif (wins >= 100000000):
            document.write(str(wins) + " ")
        elif (wins >= 10000000):
            document.write(str(wins) + "  ")
        elif (wins >= 1000000):
            document.write(str(wins) + "   ")
        elif (wins >= 100000):
            document.write(str(wins) + "    ")
        elif (wins >= 10000):
            document.write(str(wins) + "     ")
        elif (wins >= 1000):
            document.write(str(wins) + "      ")
        elif (wins >= 100):
            document.write(str(wins) + "       ")
        elif (wins >= 10):
            document.write(str(wins) + "        ")
        else:
            document.write(str(wins) + "         ")
            
        document.write(str(losses))

def print_aces_up_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Name:')
    print(Fore.BLUE + ' -')
    
def print_aces_up_score():
    with open("Name_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nName Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)
        
def print_cards(cs):
    pass
    
def valid_command(command, cs):
    validCommands = []
    return True, ''
    
def perform_action(command, cs):
    pass
    
class Card_Status():
    def __init__(self):
        #Shuffle a deck
        unshuffledDeck = ["[A D]","[A H]","[A C]","[A S]","[2 D]","[2 H]","[2 C]",
        "[2 S]","[3 D]","[3 H]","[3 C]","[3 S]","[4 D]","[4 H]","[4 C]","[4 S]","[5 D]",
        "[5 H]","[5 C]","[5 S]","[6 D]","[6 H]","[6 C]","[6 S]","[7 D]","[7 H]","[7 C]",
        "[7 S]","[8 D]","[8 H]","[8 C]","[8 S]","[9 D]","[9 H]","[9 C]","[9 S]","[10D]",
        "[10H]","[10C]","[10S]","[J D]","[J H]","[J C]","[J S]","[Q D]","[Q H]","[Q C]",
        "[Q S]","[K D]","[K H]","[K C]","[K S]"]
    
        self.deck = []
        self.flippedDeck = []
        for x in range(len(unshuffledDeck)):
            newCard = unshuffledDeck.pop(random.randint(0,len(unshuffledDeck)-1))
            self.deck.append(newCard)
            
def play_Name():
    
    #Print valid commands
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.')
    
    #Initialize cards
    cs = Card_Status()
    
    #Game loop
    gameOver = False
    while not(gameOver):
        
        #Print cards
        print_cards(cs)
        
        #Get command
        command = input("Command: ")
        
        validCommand, reason = valid_command(command, cs)
        if command == "end game":
            gameOver = True
        elif command == "view rules":
            print_Name_rules()
        elif validCommand:
            perform_action(command, cs)
        else:
            print(Fore.RED + reason)
        
        #Check if win or lose
        '''if (condition for losing):
            print(Fore.RED + "\nYou lose.")
            gameOver = True
            add_win_or_loss(False)
        if (condition for winning):
            print(Fore.GREEN + "You win!")
            gameOver = True
            add_win_or_loss(True)'''

play_Name()

''' Steps to set up a new game:
    -Ctrl F to find all instances of "Name" and change it to the name of the game.
    -Create a new text document called "(name of game)_Card_Game_Score"
    -In the print_Name_rules function ,write the rules of the game including how it works, and what to input.
    -In the Card_Status class, it shuffles a deck already. You need to split it up into piles depending on how the game works.
     If you need to you may create a "deal" function to do this repeatedly.
    -Next, in the valid_command function, make a list of all the valid commands in the validCommands variable.
     If this is impracticle, use if statements to decide if the command is valid.
     Then return True, '' if it is valid, or False, 'reason it is invalid' if it is invalid.
    -In the perform_action function, do whatever the command is supposed to do.
    -At the end of the play_Name function, take away the apostrophes to make it not a comment. Then put the conditions for winning and losing.
    -Take away the call to the play_Name function at the end and in the Card_Games file, add the following text  to the condition, with all instances of Name changed to the name of the game.
        elif (command == "rules Name"):
            print_Name_rules()
        elif (command == "play Name"):
            play_Name()
        elif (command == "score Name"):
            print_Name_score()
    -In that file, add the following text to the print statement with the other game names.
        \n -Name
    -Delete these instructions'''
