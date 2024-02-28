import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Egyptian_War_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Egyptian_War_Card_Game_Score.txt", "w") as document:
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

def print_egyptian_war_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Egptian War:')
    print(Fore.BLUE + ' -Cards are split evenly into two decks, and players take turns placing cards in the center pile.')
    print(Fore.BLUE + " -The blue name indicates who's turn it is.")
    print(Fore.BLUE + ' -If a face card is played, the other player has a certain number of cards to play another face card.')
    print(Fore.BLUE + " -A's are 5 attempts, K's are 3 attempts, Q's are 2 attempts, and J's are 1 attempt.")
    print(Fore.BLUE + " -If the player does not play a face card in the specified attempts, the cards in the pile go into the other player's deck.")
    print(Fore.BLUE + ' -Whoever gets all of the cards into their hand first wins.')
    print(Fore.BLUE + ' -To play, just hit enter, and it will simulate play. It is all luck.')
    print(Fore.BLUE + ' -Type "simulate" to quickly finish the game, or type "simulate real" to simulate a game with your own deck.')
    print(Fore.BLUE + ' -Type "end game" at any time to stop playing.')
    
def print_egyptian_war_score():
    with open("Egyptian_War_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nEgyptian War Score:")
        print(Fore.BLUE + " -Total Player 1 Wins: " + wins)
        print(Fore.BLUE + " -Total Player 2 Wins: " + losses)

def print_cards(cardStatus):
    
    if cardStatus.turn == 1:
        player1 = Fore.BLUE + "Player 1:" + Fore.RESET
        player2 = "Player 2:"
    else:
        player2 = Fore.BLUE + "Player 2:" + Fore.RESET
        player1 = "Player 1:"
    
    print("\n" + player1 + "   Pile:       " + player2 + "          Turn number: " + str(cardStatus.turnNumber))
    
    if len(cardStatus.deck1) > 0:
        if len(cardStatus.deck1) > 9:
            deck1Top = str(len(cardStatus.deck1))
        else:
            deck1Top = " " + str(len(cardStatus.deck1))
        deck1Top += Fore.BLACK + Back.WHITE + "[   ]" + Fore.RESET + Back.RESET
    else:
        deck1Top = "     "
    if len(cardStatus.deck2) > 0:
        if len(cardStatus.deck2) > 9:
            deck2Top = str(len(cardStatus.deck2))
        else:
            deck2Top = " " + str(len(cardStatus.deck2))
        deck2Top += Fore.BLACK + Back.WHITE + "[   ]" + Fore.RESET + Back.RESET
    else:
        deck2Top = "     "
    if len(cardStatus.pile) > 0:
        if len(cardStatus.pile) > 9:
            pileTop = str(len(cardStatus.pile))
        else:
            pileTop = " " + str(len(cardStatus.pile))
        if cardStatus.pile[0][3:4] == "C" or cardStatus.pile[0][3:4] == "S":
            pileTop += Fore.BLACK + Back.WHITE + cardStatus.pile[0] + Fore.RESET + Back.RESET
        else:
            pileTop += Fore.RED + Back.WHITE + cardStatus.pile[0] + Fore.RESET + Back.RESET
    else:
        pileTop = "0      "
    print(deck1Top + "     " + pileTop + "     " + deck2Top)
    if not(cardStatus.noFaceCards):
        print("      Attempts left: " + str(cardStatus.attempts))
   
def switch_turn(cs):
    if cs.turn == 1:
        cs.turn = 2
    else:
        cs.turn = 1
    
def move_cards(cs):
    cs.turnNumber += 1
    
    if cs.turn == 1:
        cs.pile.insert(0, cs.deck1.pop(0))
    else:
        cs.pile.insert(0, cs.deck2.pop(0))
       
    if cs.pile[0][1:2] == "A":
        switch_turn(cs)
        cs.attempts = 5
        cs.noFaceCards = False
    elif cs.pile[0][1:2] == "K":
        switch_turn(cs)
        cs.attempts = 3
        cs.noFaceCards = False
    elif cs.pile[0][1:2] == "Q":
        switch_turn(cs)
        cs.attempts = 2
        cs.noFaceCards = False
    elif cs.pile[0][1:2] == "J":
        switch_turn(cs)
        cs.attempts = 1
        cs.noFaceCards = False
    elif cs.noFaceCards:
        switch_turn(cs)
    else:
        cs.attempts -= 1
        
    if cs.attempts <= 0:
        cs.attempts = 1
        cs.noFaceCards = True
        for x in range(0, len(cs.pile)):
            if cs.turn == 1:
                cs.deck2.append(cs.pile.pop(len(cs.pile) - 1))
            else:
                cs.deck1.append(cs.pile.pop(len(cs.pile) - 1))
        switch_turn(cs)
    
def prepare_simulate(cs):
    print(Fore.BLUE + "\nHow to simulate your own game:")
    print(Fore.BLUE + ' -Shuffle a real deck of cards and deal into 2 hands.')
    print(Fore.BLUE + ' -Input each card, from top to bottom with cards facing down for hand 1 then 2.')
    print(Fore.BLUE + ' -Example inputs: "A C" or "10H"')
    print(Fore.BLUE + ' -The game will be simulated and it will tell you who will win in how many turns.')
    print(Fore.BLUE + ' -Type "end game" at any time to cancel.\n')
    
    cs.turnNumber = 0
    cs.noFaceCards = True
    cs.attempts = 1
    cs.pile = []
    cs.deck1 = []
    cs.deck2 = []
        
    validCards = ["[A D]","[A H]","[A C]","[A S]","[2 D]","[2 H]","[2 C]",
        "[2 S]","[3 D]","[3 H]","[3 C]","[3 S]","[4 D]","[4 H]","[4 C]","[4 S]","[5 D]",
        "[5 H]","[5 C]","[5 S]","[6 D]","[6 H]","[6 C]","[6 S]","[7 D]","[7 H]","[7 C]",
        "[7 S]","[8 D]","[8 H]","[8 C]","[8 S]","[9 D]","[9 H]","[9 C]","[9 S]","[10D]",
        "[10H]","[10C]","[10S]","[J D]","[J H]","[J C]","[J S]","[Q D]","[Q H]","[Q C]",
        "[Q S]","[K D]","[K H]","[K C]","[K S]"]    
    
    cs.canceledGame = False
    for x in range(1, 27):
        validCard = False
        while validCard == False and not(cs.canceledGame):
            newCard = input("Deck 1 Card " + str(x) + ": ")
            if newCard == "end game":
                cs.canceledGame = True
            if not(cs.canceledGame):
                for card in validCards:
                    if newCard == card[1:4]:
                        validCard = True
                        cs.deck1.append(card)
                        validCards.remove(card)
                if validCard == False:
                    print(Fore.RED + "That is not a valid card.")
        
    print("")
        
    for x in range(1, 27):
        validCard = False
        while validCard == False and not(cs.canceledGame):
            newCard = input("Deck 2 Card " + str(x) + ": ")
            if newCard == "end game":
                cs.canceledGame = True
            if not(cs.canceledGame):
                for card in validCards:
                    if newCard == card[1:4]:
                        validCard = True
                        cs.deck2.append(card)
                        validCards.remove(card)
                if validCard == False:
                    print(Fore.RED + "That is not a valid card.")
    
    if not(cs.canceledGame):
        noTurnEstablished = True
        while noTurnEstablished:
            cs.turn = input("Who goes first (type 1 or 2): ")
            if cs.turn == "1" or cs.turn == "2":
                noTurnEstablished = False
                cs.turn = int(cs.turn)
    
class Card_Status():
    def __init__(self):
        #Shuffle a deck
        unshuffledDeck = ["[A D]","[A H]","[A C]","[A S]","[2 D]","[2 H]","[2 C]",
        "[2 S]","[3 D]","[3 H]","[3 C]","[3 S]","[4 D]","[4 H]","[4 C]","[4 S]","[5 D]",
        "[5 H]","[5 C]","[5 S]","[6 D]","[6 H]","[6 C]","[6 S]","[7 D]","[7 H]","[7 C]",
        "[7 S]","[8 D]","[8 H]","[8 C]","[8 S]","[9 D]","[9 H]","[9 C]","[9 S]","[10D]",
        "[10H]","[10C]","[10S]","[J D]","[J H]","[J C]","[J S]","[Q D]","[Q H]","[Q C]",
        "[Q S]","[K D]","[K H]","[K C]","[K S]"]
    
        self.canceledGame = False
        self.simulate = False
        self.turnNumber = 1
        self.noFaceCards = True
        self.turn = random.randint(1,2)
        self.attempts = 1
        self.deck = []
        self.pile = []
        for x in range(len(unshuffledDeck)):
            newCard = unshuffledDeck.pop(random.randint(0,len(unshuffledDeck)-1))
            self.deck.append(newCard)
            
        #Split cards into 2 piles
        self.deck1 = []
        self.deck2 = []
        for x in range(0,26):
            self.deck1.append(self.deck.pop(0))
            self.deck2.append(self.deck.pop(0))
    
def play_egyptian_war():
    print('\n\nType "simulate" to speed up the game. Type "simulate real" to see who will win with your own deck. \nType "end game" to stop playing. Type "view rules" to see the rules.')
    
    #Initialize cards
    cardStatus = Card_Status()
    
    #Game loop
    gameOver = False
    while not(gameOver) and not(cardStatus.canceledGame):
        
        #Print cards
        print_cards(cardStatus)
        if cardStatus.simulate:
            command = ""
        else:
            command = input("Command: ")
        
        if command == "end game":
            gameOver = True
        elif command == "view rules":
            print_egyptian_war_rules()
        elif command == "simulate real":
            cardStatus.simulate = True
            prepare_simulate(cardStatus)
        elif command == "simulate":
            cardStatus.simulate = True
        else:
            move_cards(cardStatus)
            
        #Check if won
        if not(cardStatus.canceledGame):
            if len(cardStatus.deck2) <= 0:
                print_cards(cardStatus)
                print(Fore.GREEN + "\nPlayer 1 wins in " + str(cardStatus.turnNumber) + " turns.")
                cardStatus.simulate = False
                gameOver = True
                add_win_or_loss(True)
            if len(cardStatus.deck1) <= 0:
                print_cards(cardStatus)
                print(Fore.RED + "\nPlayer 2 wins in " + str(cardStatus.turnNumber) + " turns.")
                cardStatus.simulate = False
                gameOver = True
                add_win_or_loss(False)
