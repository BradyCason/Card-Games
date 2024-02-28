import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Aces_Up_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Aces_Up_Card_Game_Score.txt", "w") as document:
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
    print(Fore.BLUE + '\n\nHow to play Aces Up:')
    print(Fore.BLUE + ' -Cards are delt into 4 piles.')
    print(Fore.BLUE + ' -The object of the game is to get rid of all cards except for the 4 aces.')
    print(Fore.BLUE + ' -Only the cards on top of a pile (card closest to the bottom) are playable.')
    print(Fore.BLUE + ' -You can get rid of a playable card if there is another playable card in the same suit with a higher value.')
    print(Fore.BLUE + " -J's are 11, Q's are 12, K's are 13 and A's are 14.")
    print(Fore.BLUE + ' -To get rid of a card type the letter of the pile.')
    print(Fore.BLUE + ' -You may move a playable card to a spot with not cards in it.')
    print(Fore.BLUE + ' -To do this, type the letter of the pile of the card you want to move, followed by a space, \n  and then the letter of the pile of the destination.')
    print(Fore.BLUE + ' -Type "flip" to place a card from the deck on each pile.')
    print(Fore.BLUE + ' -Once you flip through all of the cards, if only the aces are left, you win.')
    
def print_aces_up_score():
    with open("Aces_Up_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nSolitaire Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)
        
def print_cards(cs):
    lines = []
    while len(lines) < len(cs.piles[0]) or len(lines) < len(cs.piles[1]) or len(lines) < len(cs.piles[2]) or len(lines) < len(cs.piles[3]):
        newLine = ''
        for number in range(0,4):
            if len(cs.piles[number]) > len(lines):
                if cs.piles[number][len(cs.piles[number]) - len(lines) - 1][3:4] == "C" or cs.piles[number][len(cs.piles[number]) - len(lines) - 1][3:4] == "S":
                    newLine += Fore.BLACK + Back.WHITE + cs.piles[number][len(cs.piles[number]) - len(lines) - 1] + Fore.RESET + Back.RESET + " "
                else:
                    newLine += Fore.RED + Back.WHITE + cs.piles[number][len(cs.piles[number]) - len(lines) - 1] + Fore.RESET + Back.RESET + " "
            else:
                newLine += "      "
        lines.append(newLine)
    
    print("   A     B     C     D")
    
    for line in lines:
        print(" " + line)
    
    print(" Cards in deck: " + str(len(cs.deck)))
    
def get_number(card):
    if card[1:3] == "A ":
        cardNumber = 14
    elif card[1:3] == "J ":
        cardNumber = 11
    elif card[1:3] == "Q ":
        cardNumber = 12
    elif card[1:3] == "K ":
        cardNumber = 13
    else:
        cardNumber = int(card[1:3].strip())
        
    return cardNumber
    
def get_cards_of_suit(suit, cs):
    cards = []
    for number in range(0,4):
        if len(cs.piles[number]) > 0:
            if cs.piles[number][0][3:4] == suit:
                cards.append(get_number(cs.piles[number][0]))
            
    return cards
    
def valid_command(command, cs):
    validCommands = ["A","B","C","D","A B","A C","A D","B A","B C","B D","C A","C B","C D","D A","D B","D C"]
    valid = False
    for validCommand in validCommands:
        if command == validCommand:
            valid = True
            
    if not(valid):
        return False, "That is not a valid command."
    
    if command[0:1] == "A":
        number = 0
    elif command[0:1] == "B":
        number = 1
    elif command[0:1] == "C":
        number = 2
    elif command[0:1] == "D":
        number = 3
    if len(cs.piles[number]) == 0:
        return False, "There are no cards in that pile."
    
    if len(command) > 1:
        if command[2:3] == "A":
            number = 0
        elif command[2:3] == "B":
            number = 1
        elif command[2:3] == "C":
            number = 2
        elif command[2:3] == "D":
            number = 3
        if len(cs.piles[number]) != 0:
            return False, "There must be no cards in the recieving pile to move a card."
        else:
            return True, ""
            
    else:
        cards = get_cards_of_suit(cs.piles[number][0][3:4], cs) #return list of values of the suit
        cardNumber = get_number(cs.piles[number][0])
            
        for card in cards:
            if cardNumber < card:
                return True, ""
        
        return False, "You cannot move that card. It is the highest of its suit."
    
def perform_action(command, cs):
    if command == "flip":
        for number in range(0,4):
            cs.piles[number].insert(0, cs.deck.pop())
    else:
    
        if command[0:1] == "A":
            pile1Number = 0
        elif command[0:1] == "B":
            pile1Number = 1
        elif command[0:1] == "C":
            pile1Number = 2
        elif command[0:1] == "D":
            pile1Number = 3
    
        if len(command) > 1:
            if command[2:3] == "A":
                pile2Number = 0
            elif command[2:3] == "B":
                pile2Number = 1
            elif command[2:3] == "C":
                pile2Number = 2
            elif command[2:3] == "D":
                pile2Number = 3
            
            cs.piles[pile2Number].insert(0, cs.piles[pile1Number].pop(0))
        else:
            cs.piles[pile1Number].pop(0)
            
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
            
        #Create piles
        self.piles = []
        for x in range(0,4):
            self.piles.append([self.deck.pop(0)])
            
def play_aces_up():
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.\n')
    
    #Initialize cards
    cs = Card_Status()
    
    #Game loop
    gameOver = False
    while not(gameOver):
        
        #Print cards
        print_cards(cs)
        
        command = input("Command: ")
        
        #Check if won or lost
        if len(cs.deck) <= 0 and command == "flip":
            won = True
            for number in range(0,4):
                if not(len(cs.piles[number]) == 1 and cs.piles[number][0][1:2] == "A"):
                    won = False
            if won:
                print(Fore.GREEN + "You win!")
                gameOver = True
                add_win_or_loss(True)
            else:
                print(Fore.RED + "\nYou lose.")
                gameOver = True
                add_win_or_loss(False)
        else:
        
            validCommand, reason = valid_command(command, cs)
        
            if command == "end game":
                cs.gameOver = True
            elif command == "view rules":
                print_aces_up_rules()
                print('')
            elif command == "flip":
                perform_action(command, cs)
            elif validCommand:
                perform_action(command, cs)
            else:
                print(Fore.RED + reason)
        
