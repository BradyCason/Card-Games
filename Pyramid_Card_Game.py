import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def prep_cards():
    
    #Shuffle a deck
    unshuffledDeck = ["[ A ]","[ A ]","[ A ]","[ A ]","[ 2 ]","[ 2 ]","[ 2 ]",
        "[ 2 ]","[ 3 ]","[ 3 ]","[ 3 ]","[ 3 ]","[ 4 ]","[ 4 ]","[ 4 ]","[ 4 ]","[ 5 ]",
        "[ 5 ]","[ 5 ]","[ 5 ]","[ 6 ]","[ 6 ]","[ 6 ]","[ 6 ]","[ 7 ]","[ 7 ]","[ 7 ]",
        "[ 7 ]","[ 8 ]","[ 8 ]","[ 8 ]","[ 8 ]","[ 9 ]","[ 9 ]","[ 9 ]","[ 9 ]","[10 ]",
        "[10 ]","[10 ]","[10 ]","[ J ]","[ J ]","[ J ]","[ J ]","[ Q ]","[ Q ]","[ Q ]",
        "[ Q ]","[ K ]","[ K ]","[ K ]","[ K ]"]
    
    deck = []
    for x in range(len(unshuffledDeck)):
        newCard = unshuffledDeck.pop(random.randint(0,len(unshuffledDeck)-1))
        deck.append(newCard)
    
    #Assign cards to a row
    row1 = "A                   " + deck.pop(0)
    row2 = "B                " + deck.pop(0) + " " + deck.pop(0)
    row3 = "C             " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0)
    row4 = "D          " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0)
    row5 = "E       " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0)
    row6 = "F    " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0)
    row7 = "G " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0) + " " + deck.pop(0)
    
    #Return all values
    return(deck, row1, row2, row3, row4, row5, row6, row7)

def print_pyramid_rules():
    
    #Print rules
    print(Fore.BLUE + "\n\nHow to play Pyramid:")
    print(Fore.BLUE + " -Match 2 available cards cards (ones without cards below them) that add up to 13 to take them away.")
    print(Fore.BLUE + " -J's are 11, Q's are 12, and K's go away by themselves.")
    print(Fore.BLUE + " -Take away all cards in the pyramid to win.")
    print(Fore.BLUE + " -To choose a card, type the letter of the row on the left and the number of cards to the right it is.")
    print(Fore.BLUE + " -When counting to the right, cards that are gone are still counted.")
    print(Fore.BLUE + " -Type a space and do the same for the second card")
    print(Fore.BLUE + " -Example: B2 C1")
    print(Fore.BLUE + " -To take away a King, type only one card")
    print(Fore.BLUE + ' -If you have no options, type "flip" to flip the top card of the deck.')
    print(Fore.BLUE + " -If you flip all the cards in the deck without discarding any, you lose.")
    print(Fore.BLUE + ' -Type "end game" at any time to stop playing.')

def print_pyramid_score():
    with open("Pyramid_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nPyramid Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)

def print_cards(row1, row2, row3, row4, row5, row6, row7, deck):
    print("\n" + row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    print("H Cards in Deck: " + str(len(deck)) + "      Top of Deck: " + deck[0] )
    
def find_cards(command, row1, row2, row3, row4, row5, row6, row7, topOfDeck):
    #Find first card
    first_card = ""
    if command[0:1] == "A":
        if command[1:2] == "1":
            first_card = row1[20:25]
    if command[0:1] == "B":
        if command[1:2] == "1":
            first_card = row2[17:22]
        if command[1:2] == "2":
            first_card = row2[23:28]
    if command[0:1] == "C":
        if command[1:2] == "1":
            first_card = row3[14:19]
        if command[1:2] == "2":
            first_card = row3[20:25]
        if command[1:2] == "3":
            first_card = row3[26:31]
    if command[0:1] == "D":
        if command[1:2] == "1":
            first_card = row4[11:16]
        if command[1:2] == "2":
            first_card = row4[17:22]
        if command[1:2] == "3":
            first_card = row4[23:28]
        if command[1:2] == "4":
            first_card = row4[29:34]
    if command[0:1] == "E":
        if command[1:2] == "1":
            first_card = row5[8:13]
        if command[1:2] == "2":
            first_card = row5[14:19]
        if command[1:2] == "3":
            first_card = row5[20:25]
        if command[1:2] == "4":
            first_card = row5[26:31]
        if command[1:2] == "5":
            first_card = row5[32:37]
    if command[0:1] == "F":
        if command[1:2] == "1":
            first_card = row6[5:10]
        if command[1:2] == "2":
            first_card = row6[11:16]
        if command[1:2] == "3":
            first_card = row6[17:22]
        if command[1:2] == "4":
            first_card = row6[23:28]
        if command[1:2] == "5":
            first_card = row6[29:34]
        if command[1:2] == "6":
            first_card = row6[35:40]
    if command[0:1] == "G":
        if command[1:2] == "1":
            first_card = row7[2:7]
        if command[1:2] == "2":
            first_card = row7[8:13]
        if command[1:2] == "3":
            first_card = row7[14:19]
        if command[1:2] == "4":
            first_card = row7[20:25]
        if command[1:2] == "5":
            first_card = row7[26:31]
        if command[1:2] == "6":
            first_card = row7[32:37]
        if command[1:2] == "7":
            first_card = row7[38:43]
    if command[0:1] == "H":
        if command[1:2] == "1":
            first_card = topOfDeck
    
    #Find second card
    second_card = ""
    if command[3:4] == "A":
        if command[4:5] == "1":
            second_card = row1[20:25]
    if command[3:4] == "B":
        if command[4:5] == "1":
            second_card = row2[17:22]
        if command[4:5] == "2":
            second_card = row2[23:28]
    if command[3:4] == "C":
        if command[4:5] == "1":
            second_card = row3[14:19]
        if command[4:5] == "2":
            second_card = row3[20:25]
        if command[4:5] == "3":
            second_card = row3[26:31]
    if command[3:4] == "D":
        if command[4:5] == "1":
            second_card = row4[11:16]
        if command[4:5] == "2":
            second_card = row4[17:22]
        if command[4:5] == "3":
            second_card = row4[23:28]
        if command[4:5] == "4":
            second_card = row4[29:34]
    if command[3:4] == "E":
        if command[4:5] == "1":
            second_card = row5[8:13]
        if command[4:5] == "2":
            second_card = row5[14:19]
        if command[4:5] == "3":
            second_card = row5[20:25]
        if command[4:5] == "4":
            second_card = row5[26:31]
        if command[4:5] == "5":
            second_card = row5[32:37]
    if command[3:4] == "F":
        if command[4:5] == "1":
            second_card = row6[5:10]
        if command[4:5] == "2":
            second_card = row6[11:16]
        if command[4:5] == "3":
            second_card = row6[17:22]
        if command[4:5] == "4":
            second_card = row6[23:28]
        if command[4:5] == "5":
            second_card = row6[29:34]
        if command[4:5] == "6":
            second_card = row6[35:40]
    if command[3:4] == "G":
        if command[4:5] == "1":
            second_card = row7[2:7]
        if command[4:5] == "2":
            second_card = row7[8:13]
        if command[4:5] == "3":
            second_card = row7[14:19]
        if command[4:5] == "4":
            second_card = row7[20:25]
        if command[4:5] == "5":
            second_card = row7[26:31]
        if command[4:5] == "6":
            second_card = row7[32:37]
        if command[4:5] == "7":
            second_card = row7[38:43]
    if command[3:4] == "H":
        if command[4:5] == "1":
            second_card = topOfDeck
    
    return(first_card, second_card)

def adds_up_to_13(firstCard, secondCard):
    
    #Return True if they add up to 13.
    if (firstCard == "[ A ]" and secondCard == "[ Q ]"):
        return(True)
    if (firstCard == "[ 2 ]" and secondCard == "[ J ]"):
        return(True)
    if (firstCard == "[ 3 ]" and secondCard == "[10 ]"):
        return(True)
    if (firstCard == "[ 4 ]" and secondCard == "[ 9 ]"):
        return(True)
    if (firstCard == "[ 5 ]" and secondCard == "[ 8 ]"):
        return(True)
    if (firstCard == "[ 6 ]" and secondCard == "[ 7 ]"):
        return(True)
    if (firstCard == "[ 7 ]" and secondCard == "[ 6 ]"):
        return(True)
    if (firstCard == "[ 8 ]" and secondCard == "[ 5 ]"):
        return(True)
    if (firstCard == "[ 9 ]" and secondCard == "[ 4 ]"):
        return(True)
    if (firstCard == "[10 ]" and secondCard == "[ 3 ]"):
        return(True)
    if (firstCard == "[ J ]" and secondCard == "[ 2 ]"):
        return(True)
    if (firstCard == "[ Q ]" and secondCard == "[ A ]"):
        return(True)
    if (firstCard == "[ K ]" and secondCard == ""):
        return(True)
    if (firstCard == "" and secondCard == "[ K ]"):
        return(True)
    return(False)

def is_valid_command(command, firstCard, secondCard):
    availableCommands = ["A1", "B1", "B2", "C1", "C2", "C3", "D1", "D2", "D3", "D4", "E1", "E2", "E3", "E4", "E5", 
        "F1", "F2", "F3", "F4", "F5", "F6", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "H1"]
    
    validCommand = True
    
    #If second card has nothing
    if (command[4:5] == ""):
        validCommand = False
        
    #If first card is a real card
    firstCardIsReal = False
    for x in availableCommands:
        if (command[0:2] == x):
            firstCardIsReal = True
    #If second card is a real card
    secondCardIsReal = False
    for x in availableCommands:
        if (command[3:5] == x):
            secondCardIsReal = True
        
    #If first card is not real, and second one is a king
    if (not(firstCardIsReal) and secondCard == "[ K ]"):
        validCommand = True
    #If second card is not real, and first one is a king
    if (not(secondCardIsReal) and firstCard == "[ K ]"):
        validCommand = True
    
    #If cards are the same
    if (command[0:2] == command[3:5]):
        validCommand = False
    #If command is too long
    if (command[5:6] != ""):
        validCommand = False
    #If middle is not a space or nothing
    if (command[2:3] != " " and command[2:3] != ""):
        validCommand = False
        
    #If command is flip, end game, or view rules
    if (command == "flip"):
        validCommand = True
    if (command == "end game"):
        validCommand = True
    if (command == "view rules"):
        validCommand = True
            
    return(validCommand)

class Card_Status():
    
    #Keeps track of which cards are live
    
    def __init__(self):
        #card : [is it live?, card down and left, card down and right]
        self.cards = {"A1":["Not Gone", "B1", "B2"], "B1":["Not Gone", "C1", "C2"], "B2":["Not Gone", "C2", "C3"], "C1":["Not Gone", "D1", "D2"], "C2":["Not Gone","D2", "D3"], "C3":["Not Gone", "D3", "D4"],
            "D1":["Not Gone", "E1", "E2"], "D2":["Not Gone", "E2", "E3"], "D3":["Not Gone", "E3", "E4"], "D4":["Not Gone", "E4", "E5"], "E1":["Not Gone", "F1", "F2"], "E2":["Not Gone", "F2", "F3"], 
            "E3":["Not Gone", "F3", "F4"], "E4":["Not Gone", "F4", "F5"], "E5":["Not Gone", "F5", "F6"], "F1":["Not Gone", "G1", "G2"], "F2":["Not Gone", "G2", "G3"], "F3":["Not Gone", "G3", "G4"], 
            "F4":["Not Gone", "G4", "G5"], "F5":["Not Gone", "G5", "G6"], "F6":["Not Gone", "G6", "G7"], "G1":["Not Gone", "Z", "Z"], "G2":["Not Gone", "Z", "Z"], "G3":["Not Gone", "Z", "Z"], 
            "G4":["Not Gone", "Z", "Z"], "G5":["Not Gone", "Z", "Z"], "G6":["Not Gone", "Z", "Z"], "G7":["Not Gone", "Z", "Z"], "Z":["Gone"], "H1":["Gone"]}
            
    def isLive(self, command):
        card1IsGood = False
        card2IsGood = False
        try:
            if (self.cards[self.cards[command[0:2]][1]][0] == "Gone" and self.cards[self.cards[command[0:2]][2]][0] == "Gone"):
                card1IsGood = True
        except:
            if (command[0:2] == "H1"):
                card1IsGood = True
        try:
            if (self.cards[self.cards[command[3:5]][1]][0] == "Gone" and self.cards[self.cards[command[3:5]][2]][0] == "Gone"):
                card2IsGood = True
        except:
            if (command[3:5] == "H1" or command[3:5] == ""):
                card2IsGood = True
        if (card1IsGood and card2IsGood):
            return(True)
        
        return(False)

def update_rows(command, row1, row2, row3, row4, row5, row6, row7, deck):
    
    #Convert rows to lists
    row1List= []
    for character in row1:
        row1List.append(character)
    row2List= []
    for character in row2:
        row2List.append(character)
    row3List= []
    for character in row3:
        row3List.append(character)
    row4List= []
    for character in row4:
        row4List.append(character)
    row5List= []
    for character in row5:
        row5List.append(character)
    row6List= []
    for character in row6:
        row6List.append(character)
    row7List= []
    for character in row7:
        row7List.append(character)
    deckList= []
    
    #Take away selected cards
    if (command[0:1] == "A"):
        if (command[1:2] == "1"):
            row1List[20] = " "
            row1List[21] = " "
            row1List[22] = " "
            row1List[23] = " "
            row1List[24] = " "
    elif (command[0:1] == "B"):
        if (command[1:2] == "1"):
            row2List[17] = " "
            row2List[18] = " "
            row2List[19] = " "
            row2List[20] = " "
            row2List[21] = " "
        if (command[1:2] == "2"):
            row2List[23] = " "
            row2List[24] = " "
            row2List[25] = " "
            row2List[26] = " "
            row2List[27] = " "
    elif (command[0:1] == "C"):
        if (command[1:2] == "1"):
            row3List[14] = " "
            row3List[15] = " "
            row3List[16] = " "
            row3List[17] = " "
            row3List[18] = " "
        if (command[1:2] == "2"):
            row3List[20] = " "
            row3List[21] = " "
            row3List[22] = " "
            row3List[23] = " "
            row3List[24] = " "
        if (command[1:2] == "3"):
            row3List[26] = " "
            row3List[27] = " "
            row3List[28] = " "
            row3List[29] = " "
            row3List[30] = " "
    elif (command[0:1] == "D"):
        if (command[1:2] == "1"):
            row4List[11] = " "
            row4List[12] = " "
            row4List[13] = " "
            row4List[14] = " "
            row4List[15] = " "
        if (command[1:2] == "2"):
            row4List[17] = " "
            row4List[18] = " "
            row4List[19] = " "
            row4List[20] = " "
            row4List[21] = " "
        if (command[1:2] == "3"):
            row4List[23] = " "
            row4List[24] = " "
            row4List[25] = " "
            row4List[26] = " "
            row4List[27] = " "
        if (command[1:2] == "4"):
            row4List[29] = " "
            row4List[30] = " "
            row4List[31] = " "
            row4List[32] = " "
            row4List[33] = " "
    elif (command[0:1] == "E"):
        if (command[1:2] == "1"):
            row5List[8] = " "
            row5List[9] = " "
            row5List[10] = " "
            row5List[11] = " "
            row5List[12] = " "
        if (command[1:2] == "2"):
            row5List[14] = " "
            row5List[15] = " "
            row5List[16] = " "
            row5List[17] = " "
            row5List[18] = " "
        if (command[1:2] == "3"):
            row5List[20] = " "
            row5List[21] = " "
            row5List[22] = " "
            row5List[23] = " "
            row5List[24] = " "
        if (command[1:2] == "4"):
            row5List[26] = " "
            row5List[27] = " "
            row5List[28] = " "
            row5List[29] = " "
            row5List[30] = " "
        if (command[1:2] == "5"):
            row5List[32] = " "
            row5List[33] = " "
            row5List[34] = " "
            row5List[35] = " "
            row5List[36] = " "
    elif (command[0:1] == "F"):
        if (command[1:2] == "1"):
            row6List[5] = " "
            row6List[6] = " "
            row6List[7] = " "
            row6List[8] = " "
            row6List[9] = " "
        if (command[1:2] == "2"):
            row6List[11] = " "
            row6List[12] = " "
            row6List[13] = " "
            row6List[14] = " "
            row6List[15] = " "
        if (command[1:2] == "3"):
            row6List[17] = " "
            row6List[18] = " "
            row6List[19] = " "
            row6List[20] = " "
            row6List[21] = " "
        if (command[1:2] == "4"):
            row6List[23] = " "
            row6List[24] = " "
            row6List[25] = " "
            row6List[26] = " "
            row6List[27] = " "
        if (command[1:2] == "5"):
            row6List[29] = " "
            row6List[30] = " "
            row6List[31] = " "
            row6List[32] = " "
            row6List[33] = " "
        if (command[1:2] == "6"):
            row6List[35] = " "
            row6List[36] = " "
            row6List[37] = " "
            row6List[38] = " "
            row6List[39] = " "
    elif (command[0:1] == "G"):
        if (command[1:2] == "1"):
            row7List[2] = " "
            row7List[3] = " "
            row7List[4] = " "
            row7List[5] = " "
            row7List[6] = " "
        if (command[1:2] == "2"):
            row7List[8] = " "
            row7List[9] = " "
            row7List[10] = " "
            row7List[11] = " "
            row7List[12] = " "
        if (command[1:2] == "3"):
            row7List[14] = " "
            row7List[15] = " "
            row7List[16] = " "
            row7List[17] = " "
            row7List[18] = " "
        if (command[1:2] == "4"):
            row7List[20] = " "
            row7List[21] = " "
            row7List[22] = " "
            row7List[23] = " "
            row7List[24] = " "
        if (command[1:2] == "5"):
            row7List[26] = " "
            row7List[27] = " "
            row7List[28] = " "
            row7List[29] = " "
            row7List[30] = " "
        if (command[1:2] == "6"):
            row7List[32] = " "
            row7List[33] = " "
            row7List[34] = " "
            row7List[35] = " "
            row7List[36] = " "
        if (command[1:2] == "7"):
            row7List[38] = " "
            row7List[39] = " "
            row7List[40] = " "
            row7List[41] = " "
            row7List[42] = " "
    elif (command[0:1] == "H"):
        if (command[1:2] == "1"):
            deck.pop(0)
            
    if (command[3:4] == "A"):
        if (command[4:5] == "1"):
            row1List[20] = " "
            row1List[21] = " "
            row1List[22] = " "
            row1List[23] = " "
            row1List[24] = " "
    elif (command[3:4] == "B"):
        if (command[4:5] == "1"):
            row2List[17] = " "
            row2List[18] = " "
            row2List[19] = " "
            row2List[20] = " "
            row2List[21] = " "
        if (command[4:5] == "2"):
            row2List[23] = " "
            row2List[24] = " "
            row2List[25] = " "
            row2List[26] = " "
            row2List[27] = " "
    elif (command[3:4] == "C"):
        if (command[4:5] == "1"):
            row3List[14] = " "
            row3List[15] = " "
            row3List[16] = " "
            row3List[17] = " "
            row3List[18] = " "
        if (command[4:5] == "2"):
            row3List[20] = " "
            row3List[21] = " "
            row3List[22] = " "
            row3List[23] = " "
            row3List[24] = " "
        if (command[4:5] == "3"):
            row3List[26] = " "
            row3List[27] = " "
            row3List[28] = " "
            row3List[29] = " "
            row3List[30] = " "
    elif (command[3:4] == "D"):
        if (command[4:5] == "1"):
            row4List[11] = " "
            row4List[12] = " "
            row4List[13] = " "
            row4List[14] = " "
            row4List[15] = " "
        if (command[4:5] == "2"):
            row4List[17] = " "
            row4List[18] = " "
            row4List[19] = " "
            row4List[20] = " "
            row4List[21] = " "
        if (command[4:5] == "3"):
            row4List[23] = " "
            row4List[24] = " "
            row4List[25] = " "
            row4List[26] = " "
            row4List[27] = " "
        if (command[4:5] == "4"):
            row4List[29] = " "
            row4List[30] = " "
            row4List[31] = " "
            row4List[32] = " "
            row4List[33] = " "
    elif (command[3:4] == "E"):
        if (command[4:5] == "1"):
            row5List[8] = " "
            row5List[9] = " "
            row5List[10] = " "
            row5List[11] = " "
            row5List[12] = " "
        if (command[4:5] == "2"):
            row5List[14] = " "
            row5List[15] = " "
            row5List[16] = " "
            row5List[17] = " "
            row5List[18] = " "
        if (command[4:5] == "3"):
            row5List[20] = " "
            row5List[21] = " "
            row5List[22] = " "
            row5List[23] = " "
            row5List[24] = " "
        if (command[4:5] == "4"):
            row5List[26] = " "
            row5List[27] = " "
            row5List[28] = " "
            row5List[29] = " "
            row5List[30] = " "
        if (command[4:5] == "5"):
            row5List[32] = " "
            row5List[33] = " "
            row5List[34] = " "
            row5List[35] = " "
            row5List[36] = " "
    elif (command[3:4] == "F"):
        if (command[4:5] == "1"):
            row6List[5] = " "
            row6List[6] = " "
            row6List[7] = " "
            row6List[8] = " "
            row6List[9] = " "
        if (command[4:5] == "2"):
            row6List[11] = " "
            row6List[12] = " "
            row6List[13] = " "
            row6List[14] = " "
            row6List[15] = " "
        if (command[4:5] == "3"):
            row6List[17] = " "
            row6List[18] = " "
            row6List[19] = " "
            row6List[20] = " "
            row6List[21] = " "
        if (command[4:5] == "4"):
            row6List[23] = " "
            row6List[24] = " "
            row6List[25] = " "
            row6List[26] = " "
            row6List[27] = " "
        if (command[4:5] == "5"):
            row6List[29] = " "
            row6List[30] = " "
            row6List[31] = " "
            row6List[32] = " "
            row6List[33] = " "
        if (command[4:5] == "6"):
            row6List[35] = " "
            row6List[36] = " "
            row6List[37] = " "
            row6List[38] = " "
            row6List[39] = " "
    elif (command[3:4] == "G"):
        if (command[4:5] == "1"):
            row7List[2] = " "
            row7List[3] = " "
            row7List[4] = " "
            row7List[5] = " "
            row7List[6] = " "
        if (command[4:5] == "2"):
            row7List[8] = " "
            row7List[9] = " "
            row7List[10] = " "
            row7List[11] = " "
            row7List[12] = " "
        if (command[4:5] == "3"):
            row7List[14] = " "
            row7List[15] = " "
            row7List[16] = " "
            row7List[17] = " "
            row7List[18] = " "
        if (command[4:5] == "4"):
            row7List[20] = " "
            row7List[21] = " "
            row7List[22] = " "
            row7List[23] = " "
            row7List[24] = " "
        if (command[4:5] == "5"):
            row7List[26] = " "
            row7List[27] = " "
            row7List[28] = " "
            row7List[29] = " "
            row7List[30] = " "
        if (command[4:5] == "6"):
            row7List[32] = " "
            row7List[33] = " "
            row7List[34] = " "
            row7List[35] = " "
            row7List[36] = " "
        if (command[4:5] == "7"):
            row7List[38] = " "
            row7List[39] = " "
            row7List[40] = " "
            row7List[41] = " "
            row7List[42] = " "
    elif (command[3:4] == "H"):
        if (command[4:5] == "1"):
            deck.pop(0)
    
    #Convert rows back to strings
    row1 = ""
    for character in row1List:
        row1 += character
    row2 = ""
    for character in row2List:
        row2 += character
    row3 = ""
    for character in row3List:
        row3 += character
    row4 = ""
    for character in row4List:
        row4 += character
    row5 = ""
    for character in row5List:
        row5 += character
    row6 = ""
    for character in row6List:
        row6 += character
    row7 = ""
    for character in row7List:
        row7 += character
    
    return(row1, row2, row3, row4, row5, row6, row7, deck)

def add_win_or_loss(win):
    with open("Pyramid_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Pyramid_Card_Game_Score.txt", "w") as document:
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

def play_pyramid():
    
    #Print valid commands
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.')
    
    #Prepare cards
    deck, row1, row2, row3, row4, row5, row6, row7 = prep_cards()
    cardStatus = Card_Status()
    flipsInARow = 0
    
    #Game loop
    gameOver = False
    while not(gameOver):
        
        #Prepare round's command
        print_cards(row1, row2, row3, row4, row5, row6, row7, deck)
        command = input("\nCommand: ")
        
        #Find the two selected cards
        firstCard, secondCard = find_cards(command, row1, row2, row3, row4, row5, row6, row7, deck[0])
        
        #If command works, update status and take away cards
        if (not(is_valid_command(command, firstCard, secondCard))):
            print(Fore.RED + "\nThat is not a valid command. Please view the rules if you do not understand.\n")
        elif (not(adds_up_to_13(firstCard, secondCard)) and not(command == "flip") and not(command == "end game") and not(command == "view rules")):
            print(Fore.RED + "\nThe selected cards do not add up to 13. Try Again.\n")
        elif (not cardStatus.isLive(command) and not(command == "flip") and not(command == "end game") and not(command == "view rules")):
            print(Fore.RED + "\nAt least one of the selected cards are not uncovered. Try again.\n")
        else:
            #Move top card to back if command is flip
            if (command == "flip"):
                oldTopCard = deck.pop(0)
                deck.append(oldTopCard)
                flipsInARow += 1
            elif (command == "end game"):
                gameOver = True
            elif (command == "view rules"):
                print_pyramid_rules()
            else:
                flipsInARow = 0
                cardStatus.cards[command[0:2]][0] = "Gone"
                if (firstCard != "[ K ]"):
                    cardStatus.cards[command[3:5]][0] = "Gone"
                
                row1, row2, row3, row4, row5, row6, row7, deck = update_rows(command, row1, row2, row3, row4, row5, row6, row7, deck)
            
            #Decide if game is over
            if (flipsInARow > len(deck)):
                print(Fore.RED + "\n\nYou Lose.\n\n")
                gameOver = True
                add_win_or_loss(False)
            if (cardStatus.cards["A1"][0] == "Gone"):
                print(Fore.GREEN + "\n\nYou Win!\n\n")
                gameOver = True
                add_win_or_loss(True)

