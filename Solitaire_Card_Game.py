import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Solitaire_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Solitaire_Card_Game_Score.txt", "w") as document:
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

def print_solitaire_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Solitaire:')
    print(Fore.BLUE + ' -The object of the game is to get all of the cards into piles of each suit at the top.')
    print(Fore.BLUE + ' -These piles must be made in increasing order. So A, 2, 3, etc.')
    print(Fore.BLUE + ' -Make lines of cards with declining value, alternating red and black.')
    print(Fore.BLUE + ' -To flip 3 new cards over, type "flip".')
    print(Fore.BLUE + ' -To move cards, type the letter of the column you wish to move followed by a space and then the letter of the column you wish to move it to.')
    print(Fore.BLUE + ' -Example: "E C"')
    print(Fore.BLUE + ' -Other piles are labeled with their own letters.')
    print(Fore.BLUE + ' -If you flip through all the cards without making a move, you will lose.')
    print(Fore.BLUE + ' -Type "end game" at any time to stop playing.')
    
def print_solitaire_score():
    with open("Solitaire_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nSolitaire Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)
        
def print_cards(cardStatus):
    if len(cardStatus.piles["I"]) == 2:
        clubsPile = "      "
    else:
        clubsPile = Fore.BLACK + Back.WHITE + cardStatus.piles["I"][len(cardStatus.piles["I"]) - 2] + Fore.RESET + Back.RESET + " "
    if len(cardStatus.piles["J"]) == 2:
        diamondsPile = "      "
    else:
        diamondsPile = Fore.RED + Back.WHITE + cardStatus.piles["J"][len(cardStatus.piles["J"]) - 2] + Fore.RESET + Back.RESET + " "
    if len(cardStatus.piles["K"]) == 2:
        heartsPile = "      "
    else:
        heartsPile = Fore.RED + Back.WHITE + cardStatus.piles["K"][len(cardStatus.piles["K"]) - 2] + Fore.RESET + Back.RESET + " "
    if len(cardStatus.piles["L"]) == 2:
        spadesPile = "      "
    else:
        spadesPile = Fore.BLACK + Back.WHITE + cardStatus.piles["L"][len(cardStatus.piles["L"]) - 2] + Fore.RESET + Back.RESET + " "
    
    print("\n  Clubs(I): " + clubsPile + " Diamonds(J): " + diamondsPile + " Hearts(K): " + heartsPile + " Spades(L): " + spadesPile)
    
    lines = []
    while len(lines) < cardStatus.piles["A"][0] or len(lines) < cardStatus.piles["B"][0] or len(lines) < cardStatus.piles["C"][0] or len(lines) < cardStatus.piles["D"][0] or len(lines) < cardStatus.piles["E"][0] or len(lines) < cardStatus.piles["F"][0] or len(lines) < cardStatus.piles["G"][0]:
        newLine = " "
        for letter in ["A","B","C","D","E","F","G"]:
            if len(lines) == 0:
                newLine += str(len(cardStatus.piles[letter]) - 1 - cardStatus.piles[letter][0])
            else:
                newLine += " "
            if cardStatus.piles[letter][0] >= len(lines) + 1:
                if cardStatus.piles[letter][len(lines) + 1][3:4] == "C" or cardStatus.piles[letter][len(lines) + 1][3:4] == "S":
                    newLine += Fore.BLACK + Back.WHITE + cardStatus.piles[letter][len(lines) + 1] + Fore.RESET + Back.RESET + " "
                else:
                    newLine += Fore.RED + Back.WHITE + cardStatus.piles[letter][len(lines) + 1] + Fore.RESET + Back.RESET + " "
            else:
                newLine += "      "
        
        lines.append(newLine)
    
    print('\n    A      B      C      D      E      F      G')
    for line in lines:
        print(line)
        
    if len(cardStatus.piles["H"]) == 1:
        topOfDraw = "0"
    elif cardStatus.piles["H"][1][3:4] == "C" or cardStatus.piles["H"][1][3:4] == "S":
        topOfDraw = str(len(cardStatus.piles["H"]) - 2) + Fore.BLACK + Back.WHITE + cardStatus.piles["H"][1] + Back.RESET + Fore.RESET
    else:
        topOfDraw = str(len(cardStatus.piles["H"]) - 2) + Fore.RED + Back.WHITE + cardStatus.piles["H"][1] + Back.RESET + Fore.RESET
    print("\nCards in deck: " + str(len(cardStatus.deck)) + "     Draw Pile (H): " + topOfDraw + "     Flipped cards: " + str(len(cardStatus.flippedDeck))  + "\n")
    
def valid_command(command, cardStatus):
    if command == "end game" or command == "view rules" or command == "flip":
        return True, ""
    
    firstValid = False
    secondValid = False
    for letter in ["A","B","C","D","E","F","G","H","I","J","K","L"]:
        if command[0:1] == letter:
            firstValid = True
        if command[2:3] == letter:
            secondValid = True
    if firstValid and secondValid and command[3:4] == "":
        if command[2:3] == "H":
            return False, "You may not move cards to the draw pile."
        if command[0:1] == "I" or command[0:1] == "J" or command[0:1] == "K" or command[0:1] == "L":
            return False, "You may not move cards out of the target piles."
        if command[0:1] == "H" and cardStatus.piles["H"][0] == 0:
            return False, "There are no cards in the draw pile."
        if len(cardStatus.piles[command[0:1]]) == 1:
            return False, "There are no cards in one of the selected piles."
        if len(cardStatus.piles[command[2:3]]) == 1 and cardStatus.piles[command[0:1]][1][1:2] != "K":
            return False, "There are no cards in one of the selected piles."
        return True, ""
    else:
        return False, "That is not a valid command."

def move_cards(cardStatus, start, end):
    for x in range(0, cardStatus.piles[start][0]):
        cardStatus.piles[end].insert(cardStatus.piles[end][0] + 1 + x, cardStatus.piles[start].pop(1))
    cardStatus.piles[end][0] += cardStatus.piles[start][0]
    if len(cardStatus.piles[start]) >= 2:
        cardStatus.piles[start][0] = 1
    else:
        cardStatus.piles[start][0] = 0
    
def move_card_up(cardStatus, start, end):
    cardStatus.piles[end].insert(len(cardStatus.piles[end]) - 1, cardStatus.piles[start].pop(cardStatus.piles[start][0]))
    if cardStatus.piles[start][0] >= 2:
        cardStatus.piles[start][0] -= 1
    else:
        if len(cardStatus.piles[start]) == 1:
            cardStatus.piles[start][0] = 0
        else:
            cardStatus.piles[start][0] = 1

def try_to_move_cards(start, end, cardStatus):
    
    #Get Cards
    startCard = cardStatus.piles[start][1]
    if len(cardStatus.piles[end]) == 1:
        endCard = startCard
    else:
        endCard = cardStatus.piles[end][cardStatus.piles[end][0]]
    
    #Get numbers
    startNumber = cardStatus.piles[start][1][1:3].strip()
    if len(cardStatus.piles[end]) != 1 and end != "I" and end != "J" and end != "K" and end != "L":
        endNumber = cardStatus.piles[end][cardStatus.piles[end][0]][1:3].strip()
        
    if end == "I" or end == "J" or end == "K" or end == "L":
        startCard = cardStatus.piles[start][cardStatus.piles[start][0]]
        print(startCard)
        endCard = cardStatus.piles[end][len(cardStatus.piles[end]) - 1]
        startNumber = startCard[1:3].strip()
        print(startNumber)
        if cardStatus.piles[end][len(cardStatus.piles[end]) - 2] == 0:
            endNumber = cardStatus.piles[end][len(cardStatus.piles[end]) - 1][1:3]
        else: 
            endNumber = cardStatus.piles[end][len(cardStatus.piles[end]) - 2][1:3].strip()
    
    if startNumber == "J":
        startNumber = 11
    elif startNumber == "Q":
        startNumber = 12
    elif startNumber == "K":
        startNumber = 13
    elif startNumber == "A":
        startNumber = 1
        
    if len(cardStatus.piles[end]) == 1:
        endNumber = int(startNumber) + 1
    
    if endNumber == "J":
        endNumber = 11
    elif endNumber == "Q":
        endNumber = 12
    elif endNumber == "K":
        endNumber = 13
    elif endNumber == "A":
        endNumber = 1
        
    startNumber = int(startNumber)
    if endNumber != "  ":
        endNumber = int(endNumber)
    else:
        endNumber = 0
    
    if end == "I":
        if startCard[3:4] == "C":
            if len(cardStatus.piles["I"]) == 2 and startCard == "[A C]":
                move_card_up(cardStatus, start, end)
                cardStatus.piles["I"][0] = 1
            elif startNumber == endNumber + 1:
                move_card_up(cardStatus, start, end)
            else:
                print(Fore.RED + "The selected cards do not go together.")
        else:
            print(Fore.RED + "The selected card is not a Club.")
    elif end == "J":
        if startCard[3:4] == "D":
            if len(cardStatus.piles["J"]) == 2 and startCard == "[A D]":
                move_card_up(cardStatus, start, end)
                cardStatus.piles["J"][0] = 1
            elif startNumber == endNumber + 1:
                move_card_up(cardStatus, start, end)
            else:
                print(Fore.RED + "The selected cards do not go together.")
        else:
            print(Fore.RED + "The selected card is not a Diamond.")
    elif end == "K":
        if startCard[3:4] == "H":
            if len(cardStatus.piles["K"]) == 2 and startCard == "[A H]":
                move_card_up(cardStatus, start, end)
                cardStatus.piles["K"][0] = 1
            elif startNumber == endNumber + 1:
                move_card_up(cardStatus, start, end)
            else:
                print(Fore.RED + "The selected cards do not go together.")
        else:
            print(Fore.RED + "The selected card is not a Heart.")
    elif end == "L":
        if startCard[3:4] == "S":
            if len(cardStatus.piles["L"]) == 2 and startCard == "[A S]":
                move_card_up(cardStatus, start, end)
                cardStatus.piles["L"][0] = 1
            elif startNumber == endNumber + 1:
                move_card_up(cardStatus, start, end)
            else:
                print(Fore.RED + "The selected cards do not go together.")
        else:
            print(Fore.RED + "The selected card is not a Spade.")
    else:
        if startNumber == endNumber - 1:
            if ((startCard[3:4] == "C" or startCard[3:4] == "S") and (endCard[3:4] == "D" or endCard[3:4] == "H") or (endCard[3:4] == "C" or endCard[3:4] == "S") and (startCard[3:4] == "D" or startCard[3:4] == "H")) or len(cardStatus.piles[end]) == 1:
                move_cards(cardStatus, start, end)
            else:
                print(Fore.RED + "The chosen cards are the same color.")
        else:
            print(Fore.RED + "The chosen cards do not go together.")

def flip_card(cardStatus):
    for x in range(0,len(cardStatus.piles["H"]) - 1):
        cardStatus.flippedDeck.append(cardStatus.piles["H"].pop(1))
        
    if len(cardStatus.deck) >= 3:
        y = 3
    else:
        y = len(cardStatus.deck)
    
    for x in range(0,y):
        cardStatus.piles["H"].append(cardStatus.deck.pop(0))
    
    cardStatus.piles["H"][0] = 1
    
    if len(cardStatus.deck) <= 0:
        for x in range(0,len(cardStatus.flippedDeck)):
            cardStatus.deck.append(cardStatus.flippedDeck.pop(0))

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
        
        #Create piles: "column":[number of cards showing in column, card1, card2...]
        self.piles = {"A":[1, self.deck.pop(0)],"B":[1],"C":[1],"D":[1],"E":[1],"F":[1],"G":[1], "H":[0], "I":[0, "     "], "J":[0, "     "], "K":[0, "     "], "L":[0, "     "]}
        
        for x in range(0,2):
            self.piles["B"].append(self.deck.pop(0))
        for x in range(0,3):
            self.piles["C"].append(self.deck.pop(0))
        for x in range(0,4):
            self.piles["D"].append(self.deck.pop(0))
        for x in range(0,5):
            self.piles["E"].append(self.deck.pop(0))
        for x in range(0,6):
            self.piles["F"].append(self.deck.pop(0))
        for x in range(0,7):
            self.piles["G"].append(self.deck.pop(0))
        
def play_solitaire():
    
    #Print valid commands
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.')
    
    #Initialize cards
    cardStatus = Card_Status()
    
    #Game loop
    flipsSinceMove = 0
    gameOver = False
    while not(gameOver):
        
        #Print cards
        print_cards(cardStatus)
        
        #Get command
        command = input("Command: ")
        
        validCommand, reason = valid_command(command, cardStatus)
        if validCommand:
            if command == "end game":
                gameOver = True
            elif command == "view rules":
                print_solitaire_rules()
            elif command == "flip":
                flip_card(cardStatus)
                flipsSinceMove += 1
            else:
                try_to_move_cards(command[0:1], command[2:3], cardStatus)
                flipsSinceMove = 0
        else:
            print(Fore.RED + reason)
        
        #Check if win or lose
        if flipsSinceMove >= ((len(cardStatus.deck) + len(cardStatus.flippedDeck))/3 + 1)*2:
            print(Fore.RED + "\nYou lose.")
            gameOver = True
            add_win_or_loss(False)
        if len(cardStatus.piles["I"]) == 15 and len(cardStatus.piles["J"]) == 15 and len(cardStatus.piles["K"]) == 15 and len(cardStatus.piles["L"]) == 15:
            print_cards(cardStatus)
            print(Fore.GREEN + "You win!")
            gameOver = True
            add_win_or_loss(True)

