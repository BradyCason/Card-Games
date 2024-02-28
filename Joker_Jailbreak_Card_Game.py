import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Joker_Jailbreak_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Joker_Jailbreak_Card_Game_Score.txt", "w") as document:
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

def print_joker_jailbreak_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Joker Jailbreak:')
    print(Fore.BLUE + ' -Cards are put into piles around a Joker.')
    print(Fore.BLUE + ' -The object of the game is to completely take away one of the "walls", or piles, next to him.')
    print(Fore.BLUE + ' -The number in front of each card indicates the number of cards in the pile.')
    print(Fore.BLUE + " -A's are worth 1, J's are worth 11, Q's are worth 12, and K's are worth 13.")
    print(Fore.BLUE + ' -Each card has a letter "R" or "B" to indicate color.')
    print(Fore.BLUE + ' -Match red cards with black cards to take them away.')
    print(Fore.BLUE + ' -You may use multiple red and black cards to add up to the same amount.')
    print(Fore.BLUE + ' -Example: [R 8] and [R 3] cancels out with [B 5] and [B 6] because they both add up to 11.')
    print(Fore.BLUE + ' -To enter a card, enter either "r" for red or "b" for black to indicate the color.')
    print(Fore.BLUE + ' -Then, enter the letter on the left, then the number of cards to the right it is.')
    print(Fore.BLUE + ' -Example: "r B3"')
    print(Fore.BLUE + ' -Hit enter, and then type in your next card. Repeat until you are done. Type "done" to finish the round.')
    print(Fore.BLUE + ' -If you have no options, type "flip", and a card from the deck will be placed on top of the Joker.')
    print(Fore.BLUE + ' -You must get rid of this card before you can win.')
    print(Fore.BLUE + ' -If you have more than 3 cards on top of the Joker, then you lose.')
    print(Fore.BLUE + ' -Type "end game" at any time to stop playing.')
    
def print_joker_jailbreak_score():
    with open("Joker_Jailbreak_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nJoker Jailbreak Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)

def print_cards(cardStatus):
    if len(cardStatus.piles["A1"]) == 0:
        card1 = "     "
    else:
        if cardStatus.piles["A1"][0][1:2] == "R":
            card1 = Fore.RED + Back.WHITE + cardStatus.piles["A1"][0]
        else:
            card1 = Fore.BLACK + Back.WHITE + cardStatus.piles["A1"][0]
    if len(cardStatus.piles["A2"]) == 0:
        card2 = "     "
    else:
        if cardStatus.piles["A2"][0][1:2] == "R":
            card2 = Fore.RED + Back.WHITE + cardStatus.piles["A2"][0]
        else:
            card2 = Fore.BLACK + Back.WHITE + cardStatus.piles["A2"][0]
    if len(cardStatus.piles["A3"]) == 0:
        card3 = "     "
    else:
        if cardStatus.piles["A3"][0][1:2] == "R":
            card3 = Fore.RED + Back.WHITE + cardStatus.piles["A3"][0]
        else:
            card3 = Fore.BLACK + Back.WHITE + cardStatus.piles["A3"][0]
    if len(cardStatus.piles["B1"]) == 0:
        card4 = "     "
    else:
        if cardStatus.piles["B1"][0][1:2] == "R":
            card4 = Fore.RED + Back.WHITE + cardStatus.piles["B1"][0]
        else:
            card4 = Fore.BLACK + Back.WHITE + cardStatus.piles["B1"][0]
    if len(cardStatus.piles["B2"]) == 0:
        card5 = "     "
    else:
        if cardStatus.piles["B2"][0][1:2] == "R":
            card5 = Fore.RED + Back.WHITE + cardStatus.piles["B2"][0]
        else:
            card5 = Fore.BLACK + Back.WHITE + cardStatus.piles["B2"][0]
    if len(cardStatus.piles["B3"]) == 0:
        card6 = "     "
    else:
        if cardStatus.piles["B3"][0][1:2] == "R":
            card6 = Fore.RED + Back.WHITE + cardStatus.piles["B3"][0]
        else:
            card6 = Fore.BLACK + Back.WHITE + cardStatus.piles["B3"][0]
    if len(cardStatus.piles["C1"]) == 0:
        card7 = "     "
    else:
        if cardStatus.piles["C1"][0][1:2] == "R":
            card7 = Fore.RED + Back.WHITE + cardStatus.piles["C1"][0]
        else:
            card7 = Fore.BLACK + Back.WHITE + cardStatus.piles["C1"][0]
    if len(cardStatus.piles["C2"]) == 0:
        card8 = "     "
    else:
        if cardStatus.piles["C2"][0][1:2] == "R":
            card8 = Fore.RED + Back.WHITE + cardStatus.piles["C2"][0]
        else:
            card8 = Fore.BLACK + Back.WHITE + cardStatus.piles["C2"][0]
    if len(cardStatus.piles["C3"]) == 0:
        card9 = "     "
    else:
        if cardStatus.piles["C3"][0][1:2] == "R":
            card9 = Fore.RED + Back.WHITE + cardStatus.piles["C3"][0]
        else:
            card9 = Fore.BLACK + Back.WHITE + cardStatus.piles["C3"][0]
    
    print("\nA  " + str(len(cardStatus.piles["A1"])) + card1 + Fore.RESET + Back.RESET + " " + str(len(cardStatus.piles["A2"])) + card2 + Fore.RESET + Back.RESET + " " + str(len(cardStatus.piles["A3"])) + card3)
    print("B  " + str(len(cardStatus.piles["B1"])) + card4 + Fore.RESET + Back.RESET + " " + str(len(cardStatus.piles["B2"])) + card5 + Fore.RESET + Back.RESET + " " + str(len(cardStatus.piles["B3"])) + card6)
    print("C  " + str(len(cardStatus.piles["C1"])) + card7 + Fore.RESET + Back.RESET + " " + str(len(cardStatus.piles["C2"])) + card8 + Fore.RESET + Back.RESET + " " + str(len(cardStatus.piles["C3"])) + card9)
    print("   Cards in deck: " + str(len(cardStatus.deck)) + "\n")

def valid_command(command, cardStatus):
    availableCommands = ["done", "flip", "end game", "view rules", "r A1", "r A2", "r A3", 
        "r B1", "r B2", "r B3", "r C1", "r C2", "r C3", "b A1", "b A2", 
        "b A3", "b B1", "b B2", "b B3", "b C1", "b C2", "b C3"]
    
    validCommand = False
    for x in availableCommands:
        if command == x:
            validCommand = True
            
            #If chosen pile has no cards
            if x != availableCommands[0] and x != availableCommands[1] and x != availableCommands[2] and x != availableCommands[3]:
                if len(cardStatus.piles[command[2:4]]) == 0:
                    return (False, "The pile you chose has no cards. ")
            
    if validCommand:
        if (command == "r B2" or command == "b B2") and len(cardStatus.piles["B2"]) == 1:
            return (False, "You may not use the Joker. ")
        elif command[0:1] == "r" and cardStatus.piles[command[2:4]][0][1:2] != "R":
            return (False, "The card you chose is not red. ")
        elif command[0:1] == "b" and cardStatus.piles[command[2:4]][0][1:2] != "B":
            return (False, "The card you chose is not black. ")
        elif command == "flip" and len(cardStatus.deck) == 0:
            return(False, "The are no cards in the deck. ")
        else:
            return (True, "")
    else:
        return (False, "")

def cards_add(redCards, blackCards, cardStatus):
    
    redTotal = 0
    for card in redCards:
        if cardStatus.piles[card][0] == "[r A]":
            redTotal += 1
        elif cardStatus.piles[card][0] == "[r 2]":
            redTotal += 2
        elif cardStatus.piles[card][0] == "[r 3]":
            redTotal += 3
        elif cardStatus.piles[card][0] == "[r 4]":
            redTotal += 4
        elif cardStatus.piles[card][0] == "[r 5]":
            redTotal += 5
        elif cardStatus.piles[card][0] == "[r 6]":
            redTotal += 6
        elif cardStatus.piles[card][0] == "[r 7]":
            redTotal += 7
        elif cardStatus.piles[card][0] == "[r 8]":
            redTotal += 8
        elif cardStatus.piles[card][0] == "[r 9]":
            redTotal += 9
        elif cardStatus.piles[card][0] == "[r10]":
            redTotal += 10
        elif cardStatus.piles[card][0] == "[r J]":
            redTotal += 11
        elif cardStatus.piles[card][0] == "[r Q]":
            redTotal += 12
        elif cardStatus.piles[card][0] == "[r K]":
            redTotal += 13
    
    blackTotal = 0
    for card in blackCards:
        if cardStatus.piles[card][0] == "[b A]":
            blackTotal += 1
        elif cardStatus.piles[card][0] == "[b 2]":
            blackTotal += 2
        elif cardStatus.piles[card][0] == "[b 3]":
            blackTotal += 3
        elif cardStatus.piles[card][0] == "[b 4]":
            blackTotal += 4
        elif cardStatus.piles[card][0] == "[b 5]":
            blackTotal += 5
        elif cardStatus.piles[card][0] == "[b 6]":
            blackTotal += 6
        elif cardStatus.piles[card][0] == "[b 7]":
            blackTotal += 7
        elif cardStatus.piles[card][0] == "[b 8]":
            blackTotal += 8
        elif cardStatus.piles[card][0] == "[b 9]":
            blackTotal += 9
        elif cardStatus.piles[card][0] == "[b10]":
            blackTotal += 10
        elif cardStatus.piles[card][0] == "[b J]":
            blackTotal += 11
        elif cardStatus.piles[card][0] == "[b Q]":
            blackTotal += 12
        elif cardStatus.piles[card][0] == "[b K]":
            blackTotal += 13
            
    if redTotal == blackTotal:
        return True
    else:
        return False
        
class Card_Status():
    def __init__(self):
        #Shuffle a deck
        unshuffledDeck = ["[B A]","[B A]","[R A]","[R A]","[B 2]","[B 2]","[R 2]",
            "[R 2]","[B 3]","[B 3]","[R 3]","[R 3]","[B 4]","[B 4]","[R 4]","[R 4]","[B 5]",
            "[B 5]","[R 5]","[R 5]","[B 6]","[B 6]","[R 6]","[R 6]","[B 7]","[B 7]","[R 7]",
            "[R 7]","[B 8]","[B 8]","[R 8]","[R 8]","[B 9]","[B 9]","[R 9]","[R 9]","[B10]",
            "[B10]","[R10]","[R10]","[B J]","[B J]","[R J]","[R J]","[B Q]","[B Q]","[R Q]",
            "[R Q]","[B K]","[B K]","[R K]","[R K]"]
    
        self.deck = []
        for x in range(len(unshuffledDeck)):
            newCard = unshuffledDeck.pop(random.randint(0,len(unshuffledDeck)-1))
            self.deck.append(newCard)
            
        self.piles = {"A1":[],"A2":[],"A3":[],"B1":[],"B2":["[Jok]"],"B3":[],"C1":[],"C2":[],"C3":[]}
        
        for x in range(0,3):
            self.piles["A1"].append(self.deck.pop(0))
        for x in range(0,7):
            self.piles["A2"].append(self.deck.pop(0))
        for x in range(0,3):
            self.piles["A3"].append(self.deck.pop(0))
        for x in range(0,7):
            self.piles["B1"].append(self.deck.pop(0))
        for x in range(0,7):
            self.piles["B3"].append(self.deck.pop(0))
        for x in range(0,3):
            self.piles["C1"].append(self.deck.pop(0))
        for x in range(0,7):
            self.piles["C2"].append(self.deck.pop(0))
        for x in range(0,3):
            self.piles["C3"].append(self.deck.pop(0))

def play_joker_jailbreak():
    
    #Print valid commands
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.')
    
    #Initialize cards
    cardStatus = Card_Status()
    
    #Game loop
    gameOver = False
    while not(gameOver):
        
        #Print cards
        print_cards(cardStatus)
        
        #Get commands
        command = ""
        redCards = []
        blackCards = []
        while command != "done" and command != "flip":
            command = input("Command: ")
            validCommand, reason = valid_command(command, cardStatus)
            
            if validCommand:
                if command[0:1] == "r":
                    redCards.append(command[2:4])
                elif command[0:1] == "b":
                    blackCards.append(command[2:4])
                elif command == "flip":
                    newCard = cardStatus.deck.pop(0)
                    cardStatus.piles["B2"].insert(0, newCard)
                elif command == "end game":
                    gameOver = True
                    command = "flip"
                elif command == "view rules":
                    print_joker_jailbreak_rules()
                    print_cards(cardStatus)
            else:
                print(Fore.RED + "That is not a valid command. " + reason + "Please try again.")
                command = "flip"
                
        #If cards add up to the same number, take them away
        if command == "done":
            if cards_add(redCards, blackCards, cardStatus):
                for card in redCards:
                    cardStatus.piles[card].pop(0)
                for card in blackCards:
                    cardStatus.piles[card].pop(0)
            else:
                print(Fore.RED + "The chosen cards do not add to the same number.")
        
        #Check if player has won or lost
        if len(cardStatus.piles["B2"]) >= 4:
            print(Fore.RED + "\nYou lose.")
            gameOver = True
            add_win_or_loss(False)
        if (len(cardStatus.piles["A2"]) <= 0 or len(cardStatus.piles["B1"]) <= 0 or len(cardStatus.piles["B3"]) <= 0 or len(cardStatus.piles["C2"]) <= 0) and len(cardStatus.piles["B2"]) == 1:
            print_cards(cardStatus)
            print(Fore.GREEN + "\nYou win!")
            gameOver = True
            add_win_or_loss(True)

