import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Black_Jack_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Black_Jack_Card_Game_Score.txt", "w") as document:
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

def print_black_jack_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Black Jack:')
    print(Fore.BLUE + ' -')
    
def print_black_jack_score():
    with open("Black_Jack_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nBlack Jack Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)


def print_cards(cardStatus):
    pass

def play_black_jack():
    pass
    
play_black_jack()
