import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def add_win_or_loss(win):
    with open("Go_Fish_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = int(contents[0:10].strip())
        losses = int(contents[10:].strip())
    if (win):
        wins += 1
    else:
        losses += 1
    with open("Go_Fish_Card_Game_Score.txt", "w") as document:
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

def print_go_fish_rules():
    
    #Print rules
    print(Fore.BLUE + '\n\nHow to play Go Fish:')
    print(Fore.BLUE + ' -Select the number of players (2 to 5) and if each player is a human or computer.')
    print(Fore.BLUE + ' -Each player is delt cards, and on their turn make sure no one is looking at the screen but them.')
    print(Fore.BLUE + ' -On your turn, type the player number you would like to take from then a space and then a value (A, J, Q, K, 2-10) that you have.')
    print(Fore.BLUE + ' -If they have any cards with that value, they will be transfered to you hand.')
    print(Fore.BLUE + ' -If you have all the cards of one value (4 cards), they are considered a book, and they are removed from your hand.')
    print(Fore.BLUE + ' -Once all the cards have been placed in a book, whoever has the most books wins.')
    
def print_go_fish_score():
    with open("Go_Fish_Card_Game_Score.txt", "r") as document:
        contents = document.read()
        wins = contents[0:10].strip()
        losses = contents[10:].strip()
        print(Fore.BLUE + "\n\nGo Fish Score:")
        print(Fore.BLUE + " -Total Human Wins: " + wins)
        print(Fore.BLUE + " -Total Computer Wins: " + losses)
        
def print_cards(cs):
    print("")
    if len(cs.lastPlays) != 0:
        print("Plays since last turn:")
        for line in cs.lastPlays:
            print(" -" + line)
        print("")
    
    sort(cs.currentPlayer, cs)
    print("Player " + str(cs.currentPlayer + 1) + "'s cards: ")
    line = ''
    for card in cs.hands[cs.currentPlayer]:
        line += " " + card + Fore.RESET + Back.RESET
    print(line)
    
    if len(cs.books[cs.currentPlayer]) == 0:
        line = "You have no books."
    else:
        line = "You have the following books:"
        for book in cs.books[cs.currentPlayer]:
            line += " " + book
    print(line + "\n")
    
    for number in range(0, cs.numPlayers):
        if number != cs.currentPlayer:
            line = 'Player ' + str(number + 1) + " has " + str(len(cs.hands[number])) + " cards and "
            if len(cs.books[number]) == 0:
                line += "no books."
            else:
                line += "the following books: "
                for book in cs.books[number]:
                    line += book + " "
            
            print(line)
    print("Cards in deck: " + str(len(cs.deck)))
    
def get_value(card):
    value = card[11:13]
    if value == "A ":
        value = 1
    elif value == "J ":
        value = 11
    elif value == "Q ":
        value = 12
    elif value == "K ":
        value = 13
    
    return int(value)
    
def sort(playerNumber, cs):
    sortedHand = []
    for card in cs.hands[playerNumber]:
        value = get_value(card)
        usedCard = False
        for number in range(0, len(sortedHand)):
            if value <= get_value(sortedHand[number]):
                sortedHand.insert(number, card)
                usedCard = True
                break
        if not(usedCard):
            sortedHand.insert(len(sortedHand), card)
    cs.hands[playerNumber] = sortedHand
        
def decide_winner(cs):
    winningNumber = len(cs.books[0])
    for number in range(1,cs.numPlayers):
        if len(cs.books[number]) > winningNumber:
            winningNumber = len(cs.books[number])
    winners = []
    for number in range(0,cs.numPlayers):
        if len(cs.books[number]) == winningNumber:
             winners.append(number)
    return winners
            
def valid_command(command, cs):
    if len(cs.hands[cs.currentPlayer]) == 0:
        cs.hasNoCards = True
        return True , ''
    
    validCommands = []
    for x in range(1,cs.numPlayers + 1):
        if x - 1 != cs.currentPlayer:
            validCommands.append(str(x))
    
    valid = False
    for validCommand in validCommands:
        if command[0:1] == validCommand:
            valid = True
            
    if not(valid):
        return False, "That is not a valid player number."
    else:
        valid = False
        validCommands = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        
        for validCommand in validCommands:
            if command[1:] == " " + validCommand:
                for card in cs.hands[cs.currentPlayer]:
                    if validCommand == card[11:13].strip():
                        valid = True
                
        if not(valid):
            return False, "That is not a valid card."
    return True, ''
    
def check_for_books(cs):
    sort(cs.currentPlayer, cs)
    copyOfHand = cs.hands[cs.currentPlayer].copy()
    copyOfHand.extend(("","",""))
    newBooks = []
    for i in range(0,len(cs.hands[cs.currentPlayer])):
        if copyOfHand[i][11:13] == copyOfHand[i + 3][11:13]:
            newBooks.append(copyOfHand[i][11:13])
            cs.books[cs.currentPlayer].append(copyOfHand[i][11:13].strip())
    
    cardsToRemove = []
    for value in newBooks:
        for card in cs.hands[cs.currentPlayer]:
            if card[11:13] == value:
                cardsToRemove.append(card)
    for card in cardsToRemove:
        cs.hands[cs.currentPlayer].remove(card)
    
def check_if_game_over(cs):
    #Check if game over
    totalBooks = []
    for x in range(0,cs.numPlayers):
        for book in cs.books[x]:
            totalBooks.append(book)
    if len(totalBooks) == 13:
        cs.gameOver = True
        winners = decide_winner(cs)
        if len(winners) == 1:
            if cs.kinds[winners[0]] == "human":
                print(Fore.GREEN + "Player " + str(winners[0] + 1) + " wins!")
                add_win_or_loss(True)
            else:
                print(Fore.RED + "Player " + str(winners[0] + 1) + " wins!")
                add_win_or_loss(False)
        else:
            line = "Winners:"
            green = False
            for winner in winners:
                line += "  Player " + str(winner + 1)
                if cs.kinds[winner] == "human":
                    green = True
            if green:
                print(Fore.GREEN + line)
            else:
                print(Fore.RED + line)
    
def perform_action(command, cs):
    if cs.hasNoCards:
        cs.hasNoCards = False
        print(Fore.RED + "\nYou have no cards so you cannot do anything.")
        if len(cs.lastPlays) == cs.numPlayers - 1:
            cs.lastPlays.pop(0)
        cs.lastPlays.append("Player " + str(cs.currentPlayer + 1) + " had no cards so they could not play.")
        if len(cs.deck) > 0:
            cs.hands[cs.currentPlayer].append(cs.deck.pop(0))
    else:
        
        numSwitches = 0
        switches = []
        for number in range(0, len(cs.hands[int(command[0:1]) - 1])):
            if cs.hands[int(command[0:1]) - 1][number][11:13].strip() == command[2:]:
                switches.append(number)
                numSwitches += 1
            
        #for i in range(0, len(switches)):
            #cs.hands[cs.currentPlayer].append(cs.hands[int(command[0:1]) - 1].pop(switches[i]))
    
        newSwitches = []
        for switch in switches:
            newSwitches.insert(0,switch)
        for switch in newSwitches:
            cs.hands[cs.currentPlayer].append(cs.hands[int(command[0:1]) - 1].pop(switch))
    
        line = "You were given " + str(numSwitches) + " cards from Player " + command[0:1] + "."
        if numSwitches == 0:
            if len(cs.deck) != 0:
                line += " You got 1 card from the deck."
            print("\n" + Fore.RED + line)
        else:
            print("\n" + Fore.GREEN + line)
    
        if numSwitches == 0 and len(cs.deck) > 0:
            cs.hands[cs.currentPlayer].append(cs.deck.pop(0))
    
        if len(cs.lastPlays) == cs.numPlayers - 1:
            cs.lastPlays.pop(0)
        cs.lastPlays.append("Player " + str(cs.currentPlayer + 1) + " asked Player " + command[0:1] + " for " + command[2:].strip() + "'s and received " + str(numSwitches) + " cards.")
    
    check_for_books(cs)
    
def perform_computer_action(cs):
    if len(cs.hands[cs.currentPlayer]) == 0:
        if len(cs.lastPlays) == cs.numPlayers - 1:
            cs.lastPlays.pop(0)
        cs.lastPlays.append("Player " + str(cs.currentPlayer + 1) + " had no cards so they could not play.")
        if len(cs.deck) > 0:
            cs.hands[cs.currentPlayer].append(cs.deck.pop(0))
    else:
        availablePlayers = []
        for i in range(0,cs.numPlayers):
            if i != cs.currentPlayer:
                availablePlayers.append(i)
        index = random.randint(0, len(availablePlayers) - 1)
        player = availablePlayers[index]
        
        availableValues = []
        totalValues = []
        for card in cs.hands[cs.currentPlayer]:
            used = False
            for usedValue in totalValues:
                if usedValue == card[11:13]:
                    used = True
            if not(used):
                totalValues.append(card[11:13])
                if not(card[11:13].strip() in cs.computerPlays[cs.currentPlayer]):
                    availableValues.append(card[11:13])
        if len(availableValues) == 0:
            availableValues = totalValues
            cs.computerPlays[cs.currentPlayer] = []
        
        value = availableValues[random.randint(0, len(availableValues) - 1)].strip()
        
        numSwitches = 0
        switches = []
        for number in range(0, len(cs.hands[player])):
            if cs.hands[player][number][11:13].strip() == value:
                switches.append(number)
                numSwitches += 1
                
        newSwitches = []
        for switch in switches:
            newSwitches.insert(0,switch)
        for switch in newSwitches:
            cs.hands[cs.currentPlayer].append(cs.hands[player].pop(switch))
        
        if numSwitches == 0 and len(cs.deck) > 0:
            cs.hands[cs.currentPlayer].append(cs.deck.pop(0))
            
        cs.computerPlays[cs.currentPlayer].append(value)
        if len(cs.lastPlays) == cs.numPlayers - 1:
            cs.lastPlays.pop(0)
        cs.lastPlays.append("Player " + str(cs.currentPlayer + 1) + " asked Player " + str(player + 1) + " for " + value + "'s and received " + str(numSwitches) + " cards.")
    
    check_for_books(cs)
    
class Card_Status():
    def __init__(self):
        self.gameOver = False
        self.currentPlayer = 0
        self.switchPlayers = False
        self.hasNoCards= False
        
        #Figure out how many people are playing
        foundNumber = False
        self.numPlayers = 0
        while not(foundNumber) and not(self.gameOver):
            number = input("How many players (2-5): ")
            if number == "end game":
                self.gameOver = True
            elif number == "view rules":
                print_go_fish_rules()
            elif number == "2" or number == "3" or number == "4" or number == "5":
                self.numPlayers = int(number)
                foundNumber = True
            else:
                print(Fore.RED + "That is not a valid command.")
        
        self.kinds = []
        for number in range(1, self.numPlayers + 1):
            foundKind = False
            while not(foundKind) and not(self.gameOver):
                kind = input("What kind of player is Player " + str(number) + " (human or computer): ")
                if kind == "end game":
                    self.gameOver = True
                elif kind == "view rules":
                    print_go_fish_rules()
                elif kind == "human" or kind == "computer":
                    self.kinds.append(kind)
                    foundKind = True
                else:
                    print(Fore.RED + "That is not a valid command.")
                    
        #Shuffle a deck
        unshuffledDeck = [Back.WHITE + Fore.RED + "[A D]",Back.WHITE + Fore.RED + "[A H]",Back.WHITE + Fore.BLACK + "[A C]",Back.WHITE + Fore.BLACK + "[A S]",Back.WHITE + Fore.RED + "[2 D]",Back.WHITE + Fore.RED + "[2 H]",Back.WHITE + Fore.BLACK + "[2 C]",
        Back.WHITE + Fore.BLACK + "[2 S]",Back.WHITE + Fore.RED + "[3 D]",Back.WHITE + Fore.RED + "[3 H]",Back.WHITE + Fore.BLACK + "[3 C]",Back.WHITE + Fore.BLACK + "[3 S]",Back.WHITE + Fore.RED + "[4 D]",Back.WHITE + Fore.RED + "[4 H]",Back.WHITE + Fore.BLACK + "[4 C]",Back.WHITE + Fore.BLACK + "[4 S]",Back.WHITE + Fore.RED + "[5 D]",
        Back.WHITE + Fore.RED + "[5 H]",Back.WHITE + Fore.BLACK + "[5 C]",Back.WHITE + Fore.BLACK + "[5 S]",Back.WHITE + Fore.RED + "[6 D]",Back.WHITE + Fore.RED + "[6 H]",Back.WHITE + Fore.BLACK + "[6 C]",Back.WHITE + Fore.BLACK + "[6 S]",Back.WHITE + Fore.RED + "[7 D]",Back.WHITE + Fore.RED + "[7 H]",Back.WHITE + Fore.BLACK + "[7 C]",
        Back.WHITE + Fore.BLACK + "[7 S]",Back.WHITE + Fore.RED + "[8 D]",Back.WHITE + Fore.RED + "[8 H]",Back.WHITE + Fore.BLACK + "[8 C]",Back.WHITE + Fore.BLACK + "[8 S]",Back.WHITE + Fore.RED + "[9 D]",Back.WHITE + Fore.RED + "[9 H]",Back.WHITE + Fore.BLACK + "[9 C]",Back.WHITE + Fore.BLACK + "[9 S]",Back.WHITE + Fore.RED + "[10D]",
        Back.WHITE + Fore.RED + "[10H]",Back.WHITE + Fore.BLACK + "[10C]",Back.WHITE + Fore.BLACK + "[10S]",Back.WHITE + Fore.RED + "[J D]",Back.WHITE + Fore.RED + "[J H]",Back.WHITE + Fore.BLACK + "[J C]",Back.WHITE + Fore.BLACK + "[J S]",Back.WHITE + Fore.RED + "[Q D]",Back.WHITE + Fore.RED + "[Q H]",Back.WHITE + Fore.BLACK + "[Q C]",
        Back.WHITE + Fore.BLACK + "[Q S]",Back.WHITE + Fore.RED + "[K D]",Back.WHITE + Fore.RED + "[K H]",Back.WHITE + Fore.BLACK + "[K C]",Back.WHITE + Fore.BLACK + "[K S]"]
    
        self.deck = []
        self.flippedDeck = []
        for x in range(len(unshuffledDeck)):
            newCard = unshuffledDeck.pop(random.randint(0,len(unshuffledDeck)-1))
            self.deck.append(newCard)
            
        self.lastPlays = []
        self.computerPlays = []
        self.books = []
        self.hands = []
        #Deal cards
        if self.numPlayers >= 4:
            for player in range(0,self.numPlayers):
                self.computerPlays.append([])
                self.books.append([])
                self.hands.append([self.deck.pop(0),self.deck.pop(0),self.deck.pop(0),self.deck.pop(0),self.deck.pop(0)])
        else:
            for player in range(0,self.numPlayers):
                self.computerPlays.append([])
                self.books.append([])
                self.hands.append([self.deck.pop(0),self.deck.pop(0),self.deck.pop(0),self.deck.pop(0),self.deck.pop(0),self.deck.pop(0),self.deck.pop(0)])
            
def play_go_fish():
    
    #Print valid commands
    print('\n\nType "end game" to stop playing. Type "view rules" to see the rules.')
    
    #Initialize cards
    cs = Card_Status()
    
    allComputer = True
    for kind in cs.kinds:
        if kind == "human":
            allComputer = False
    if allComputer:
        #simulation game loop
        while not(cs.gameOver):
            perform_computer_action(cs)
            if cs.currentPlayer == cs.numPlayers - 1:
                cs.currentPlayer = 0
            else:
                cs.currentPlayer += 1
            check_if_game_over(cs)
    else:
    
        print(Fore.BLUE + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIt is Player " + str(cs.currentPlayer + 1) + "'s turn. Give the computer to that player and hit enter.", end='')
        input()
        #Game loop
        while not(cs.gameOver):
            
            #Print cards
            if cs.switchPlayers:
                cs.switchPlayers = False
                print(Fore.BLUE + "\nHit enter to end your turn.", end='')
                input()
                foundPlayer = False
                while not(foundPlayer):
                    if cs.currentPlayer >= len(cs.hands) - 1:
                        cs.currentPlayer = 0
                    else:
                        cs.currentPlayer += 1
                    
                    if cs.kinds[cs.currentPlayer] == "human":
                        foundPlayer = True
                    else:
                        perform_computer_action(cs)
                print(Fore.BLUE + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIt is Player " + str(cs.currentPlayer + 1) + "'s turn. Give the computer to that player and hit enter.", end='')
                input()
            print_cards(cs)
            
            #Get command
            command = input("Command: ")
            
            validCommand, reason = valid_command(command, cs)
            if command == "end game":
                cs.gameOver = True
            elif command == "view rules":
                print_go_fish_rules()
            elif validCommand:
                perform_action(command, cs)
                cs.switchPlayers = True
            else:
                print(Fore.RED + reason + "\n")
            
            check_if_game_over(cs)

