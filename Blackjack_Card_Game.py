import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Blackjack_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Blackjack_Card_Game_Score.txt", "w") as document:
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

def print_blackjack_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Blackjack:')
    print(Fore.BLUE + ' -At the start, type the number of players who wish to play (1 to 4).')
    print(Fore.BLUE + ' -Then, each player types their bid. Each player gets 5 tokens at the start of the game.')
    print(Fore.BLUE + ' -Each person gets delt 2 cards, and the dealer gets 1 face up and 1 face down.')
    print(Fore.BLUE + ' -On your turn, type "hit" to get another card, or "stand" to pass.')
    print(Fore.BLUE + ' -You may type double on your first card of a hand to get only 1 ore card and double the outcome.')
    print(Fore.BLUE + ' -You may not split because that is hard to code.=(')
    print(Fore.BLUE + ' -The goal is to get closer to 21 than the dealer without going over.')
    print(Fore.BLUE + " -J's, Q's, and K's are worth 10, A's are worth 1 or 11, and all other cards are worth their number value.'")
    print(Fore.BLUE + ' -Play continues until all players have gotten 20 chips, or have lost all their chips.')
    print(Fore.BLUE + ' -Type "end game" at any time to stop playing.')
    
def print_blackjack_score():
    with open("Blackjack_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nBlackjack Score:")
        print(Fore.BLUE + " -Total Wins: " + wins)
        print(Fore.BLUE + " -Total Losses: " + losses)

def print_chips(cs):
    statement = ""
    for x in range(0, cs.numPlayers):
        if cs.chips[x] >= 20:
            number = Fore.GREEN + str(cs.chips[x]) + Fore.RESET
        elif cs.chips[x] <= 0:
            number = Fore.RED + str(cs.chips[x]) + Fore.RESET
        else:
            number = Fore.YELLOW + str(cs.chips[x]) + Fore.RESET
        statement += "Player " + str(int(x) + 1) + " Chips: " + number + "  "
    print("\n" + statement)

def print_results(cs):
    
    print("Resuls:")
    
    statement = " -"
    if cs.players[0][0] == "Bust":
        statement += "Dealer: " + Fore.RED + "Bust  " + Fore.RESET
    else:
        statement += "Dealer: " + Fore.GREEN + str(add_cards(cs.players[0])) + Fore.RESET + "  "
        
    for number in range(1, cs.numPlayers + 1):
        if cs.playing[number - 1]:
            if cs.players[number][0] == "Bust":
                statement += "Player " + str(number) + ": " + Fore.RED + "Bust  " + Fore.RESET
            else:
                statement += "Player " + str(number) + ": " + Fore.GREEN + str(add_cards(cs.players[number])) + Fore.RESET + "  "
    
    print(statement)
    
    statement = " -"
    for player in range(1,cs.numPlayers + 1):
        if cs.playing[player - 1]:
            if cs.players[player][0] == "Bust":
                statement += "Player " + str(player) + ": " + Fore.RED + " Lose  " + Fore.RESET
                cs.chips[player - 1] -= cs.bets[player - 1] * cs.multipliers[player - 1]
            elif cs.players[0][0] == "Bust":
                statement += "Player " + str(player) + ": " + Fore.GREEN + " Win  " + Fore.RESET
                cs.chips[player - 1] += cs.bets[player - 1] * cs.multipliers[player - 1]
            else:
                if add_cards(cs.players[player]) == add_cards(cs.players[0]):
                    statement += "Player " + str(player) + ": " + Fore.YELLOW + " Tie  " + Fore.RESET
                elif add_cards(cs.players[player]) > add_cards(cs.players[0]):
                    statement += "Player " + str(player) + ": " + Fore.GREEN + " Win  " + Fore.RESET
                    cs.chips[player - 1] += cs.bets[player - 1] * cs.multipliers[player - 1]
                else: 
                    statement += "Player " + str(player) + ": " + Fore.RED + " Lose  " + Fore.RESET
                    cs.chips[player - 1] -= cs.bets[player - 1] * cs.multipliers[player - 1]
    print(statement + "\n")

def print_dealer(cs):
    if cs.players[0][0] == "Bust":
        dealerCards = "Bust"
    else:
        if cs.players[0][0][3:4] == "S" or cs.players[0][0][3:4] == "C":
            dealerCards = Fore.BLACK + Back.WHITE + cs.players[0][0] + Fore.RESET + Back.RESET
        else:
            dealerCards = Fore.RED + Back.WHITE + cs.players[0][0] + Fore.RESET + Back.RESET
        if cs.showDealer:
            if cs.players[0][1][3:4] == "S" or cs.players[0][1][3:4] == "C":
                dealerCards += " " + Fore.BLACK + Back.WHITE + cs.players[0][1] + Fore.RESET + Back.RESET + " "
            else:
                dealerCards += " " + Fore.RED + Back.WHITE + cs.players[0][1] + Fore.RESET + Back.RESET + " "
        else:
            dealerCards += " " + Fore.BLACK + Back.WHITE + "[   ]" + Fore.RESET + Back.RESET
        for number in range(2, len(cs.players[0])):
            if cs.players[0][number][3:4] == "S" or cs.players[0][number][3:4] == "C":
                dealerCards += Fore.BLACK + Back.WHITE + cs.players[0][number] + Fore.RESET + Back.RESET + " "
            else:
                dealerCards += Fore.RED + Back.WHITE + cs.players[0][number] + Fore.RESET + Back.RESET + " "
    
    if cs.showDealer:
        dealerCards += "  Total: " + str(add_cards(cs.players[0]))
    print("\n  Dealer: " + dealerCards)

def print_cards(cs):
    print_dealer(cs)
    
    playersLine = ""
    for number in range(1, cs.numPlayers + 1):
        if cs.playing[number - 1]:
            playersLine += "\n  Player " + str(number) + ": "
            if cs.players[number][0] == "Bust":
                playersLine += "Bust "
            else:
                for card in cs.players[number]:
                    if card[3:4] == "S" or card[3:4] == "C":
                        playersLine += Fore.BLACK + Back.WHITE + card + Fore.RESET + Back.RESET + " "
                    else:
                        playersLine += Fore.RED + Back.WHITE + card + Fore.RESET + Back.RESET + " "
            playersLine += "  Total: " + str(add_cards(cs.players[number])) + "     Bet: " + str(cs.bets[number - 1])
    print(playersLine + "\n")

def add_cards(cards):
    total = 0
    numAs = 0
    for card in cards:
        if card[1:3] == "2 ":
            total += 2
        if card[1:3] == "3 ":
            total += 3
        if card[1:3] == "4 ":
            total += 4
        if card[1:3] == "5 ":
            total += 5
        if card[1:3] == "6 ":
            total += 6
        if card[1:3] == "7 ":
            total += 7
        if card[1:3] == "8 ":
            total += 8
        if card[1:3] == "9 ":
            total += 9
        if card[1:3] == "10" or card[1:3] == "J " or card[1:3] == "Q " or card[1:3] == "K ":
            total += 10
        if card[1:3] == "A ":
            numAs += 1
    
    for x in range(0, numAs):
        if total >= 11:
            total += 1
        else:
            total += 11
        
    return total

def valid_command(command, cs):
    if command == "hit" or command == "stand":
        return(True, "")
    elif (command == "double" or (command == "split" and cs.players[cs.currentPlayer][0][1:3] == cs.players[cs.currentPlayer][1][1:3])) and len(cs.players[cs.currentPlayer]) == 2:
        return(True, "")
    elif len(cs.players[cs.currentPlayer]) == 2:
        return(False, 'That is not a valid command. Valid commands for this situation are: "hit", "stand", "double", or "split".')
    else:
        return(False, 'That is not a valid command. Valid commands for this situation are: "hit" or "stand".')

def perform_dealer_action(cs):
    cs.showDealer = True
    print_dealer(cs)
    
    doneFlipping = False
    while not(doneFlipping):
        if add_cards(cs.players[0]) <= 16:
            cs.players[0].append(cs.deck.pop(0))
            print_dealer(cs)
        else:
            doneFlipping = True
            
    if add_cards(cs.players[0]) > 21:
        cs.players[0].insert(0, "Bust")
        
    print("")
    print_results(cs)

def perform_action(command, cs):
    if command == "stand":
        cs.currentPlayer += 1
    elif command == "hit":
        cs.players[cs.currentPlayer].append(cs.deck.pop(0))
    elif command == "double":
        cs.players[cs.currentPlayer].append(cs.deck.pop(0))
        cs.multipliers[cs.currentPlayer - 1] = 2
        cs.currentPlayer += 1
    elif command == "split":
        print(Fore.RED + "Sorry. I'm not that good at coding. You can't split. =(")

def end_round(cs):
    perform_dealer_action(cs)
            
    #Check if player has lost or won
    for number in range(1, cs.numPlayers + 1):
        if cs.playing[number - 1] == True:
            if cs.chips[number - 1] >= 20:
                cs.playing[number - 1] = False
                add_win_or_loss(True)
            elif cs.chips[number - 1] <= 0:
                cs.playing[number - 1] = False
                add_win_or_loss(False)
    
    keepPlaying = False
    for playing in cs.playing:
        if playing == True:
            keepPlaying = True
            
    if keepPlaying:
        cs.deal()
    else:
        cs.gameOver = True

class Card_Status():
    def __init__(self):
        self.gameOver = False
        
        #Set up number of players
        validNumPlayers = False
        while not(validNumPlayers) and not(self.gameOver):
            printingRules = False
            self.numPlayers = input("How many players: ")
            if self.numPlayers == "end game":
                self.gameOver = True
            elif self.numPlayers == "view rules":
                print_blackjack_rules()
                print('')
                printingRules = True
            for number in ["1","2","3","4"]:
                if self.numPlayers == number:
                    validNumPlayers = True
            if not(validNumPlayers) and not(self.gameOver) and not (printingRules):
                print(Fore.RED + "That is not a valid number of players. Please type 1, 2, 3, or 4.")
        
        if not(self.gameOver):
            self.numPlayers = int(self.numPlayers)
        
            self.chips = []
            self.playing = []
            for x in range(0, self.numPlayers):
                self.chips.append(5)
                self.playing.append(True)
            
            self.deal()
    
    def deal(self):
        
        #Shuffle a deck
        unshuffledDeck = ["[A D]","[A H]","[A C]","[A S]","[2 D]","[2 H]","[2 C]",
        "[2 S]","[3 D]","[3 H]","[3 C]","[3 S]","[4 D]","[4 H]","[4 C]","[4 S]","[5 D]",
        "[5 H]","[5 C]","[5 S]","[6 D]","[6 H]","[6 C]","[6 S]","[7 D]","[7 H]","[7 C]",
        "[7 S]","[8 D]","[8 H]","[8 C]","[8 S]","[9 D]","[9 H]","[9 C]","[9 S]","[10D]",
        "[10H]","[10C]","[10S]","[J D]","[J H]","[J C]","[J S]","[Q D]","[Q H]","[Q C]",
        "[Q S]","[K D]","[K H]","[K C]","[K S]"]
        
        self.currentPlayer = 1
        self.deck = []
        for x in range(len(unshuffledDeck)):
            newCard = unshuffledDeck.pop(random.randint(0,len(unshuffledDeck)-1))
            self.deck.append(newCard)
        
        self.multipliers = []
        self.showDealer = False
        self.players = []
        self.players.append([self.deck.pop(0), self.deck.pop(0)])
        for x in range(0, self.numPlayers):
            self.multipliers.append(1)
            self.players.append([self.deck.pop(0), self.deck.pop(0)])
            
        print_chips(self)
        self.bets = []
        for player in range(1, self.numPlayers + 1):
            if self.playing[player - 1]:
                if add_cards(self.players[player]) == 21:
                    self.multipliers[player - 1] = 2
                
                printingRules = False
                valid_bet = False
                while not(valid_bet) and not(self.gameOver):
                    bet = input("Player " + str(player) + " bet: ")
                    try:
                        if bet == "end game":
                            self.gameOver = True
                        elif bet == "view rules":
                            printingRules = True
                            print_blackjack_rules()
                            print('')
                        bet = int(bet)
                        if bet <= self.chips[player - 1] and bet > 0:
                            valid_bet = True
                            self.bets.append(bet)
                        else:
                            print(Fore.RED + "Your bet must be a number of chips that you have.")
                    except:
                        if not(self.gameOver) and not(printingRules):
                            print(Fore.RED + "That is not a valid bet.")
            else:
                self.bets.append(" ")
        
def play_blackjack():
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.\n')
    
    #Initialize cards
    cs = Card_Status()
    
    #Game loop
    while not(cs.gameOver):
        
        #Print cards
        print_cards(cs)
        
        doneWithRound = True
        for number in range(cs.currentPlayer, cs.numPlayers + 1):
            if cs.playing[number - 1]:
                doneWithRound = False
        
        if not(doneWithRound):
            #Get command
            playerFound = False
            while not(playerFound):
                if not(cs.playing[cs.currentPlayer - 1]):
                    cs.currentPlayer += 1
                else:
                    playerFound = True
            
            command = input("Player " + str(cs.currentPlayer) + " command: ")
        
            validCommand, reason = valid_command(command, cs)
        
            if command == "end game":
                cs.gameOver = True
            elif command == "view rules":
                print_blackjack_rules()
                print('')
            elif validCommand:
                perform_action(command, cs)
            else:
                print(Fore.RED + reason)
        else:
            cs.currentPlayer += 1
        
        #Check if round over
        if cs.currentPlayer > cs.numPlayers:
            #Check if busted
            if add_cards(cs.players[cs.currentPlayer - 1]) > 21:
                cs.players[cs.currentPlayer].insert(0, "Bust")
            end_round(cs)
        else:
            #Check if busted
            if add_cards(cs.players[cs.currentPlayer]) > 21:
                cs.players[cs.currentPlayer].insert(0, "Bust")
                cs.currentPlayer += 1
                if cs.currentPlayer > cs.numPlayers:
                    end_round(cs)
    
