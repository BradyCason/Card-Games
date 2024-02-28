from Pyramid_Card_Game import *
from Joker_Jailbreak_Card_Game import *
from Solitaire_Card_Game import *
from Egyptian_War_Card_Game import *
from Blackjack_Card_Game import *
from Aces_Up_Card_Game import *
from Go_Fish_Card_Game import *
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def non_game_loop():
    playing = True
    while playing:
        
        #Print available commands
        print(Fore.YELLOW + '\n\nType one of the following commands:')
        print(Fore.YELLOW + ' -"score" to view the score\n -"rules" to view the rules\n -"play" to play the game')
        print(Fore.YELLOW + '\nThen type one of the following games:')
        print(Fore.YELLOW + ' -aces up\n -blackjack\n -egyptian war\n -go fish\n -joker jailbreak\n -pyramid\n -solitaire')
        print(Fore.YELLOW + '\nType "end program" to stop.\n\n')
        command = input("Command: ")
        if (command == "rules pyramid"):
            print_pyramid_rules()
        elif (command == "play pyramid"):
            play_pyramid()
        elif (command == "score pyramid"):
            print_pyramid_score()
        elif (command == "rules joker jailbreak"):
            print_joker_jailbreak_rules()
        elif (command == "play joker jailbreak"):
            play_joker_jailbreak()
        elif (command == "score joker jailbreak"):
            print_joker_jailbreak_score()
        elif (command == "rules solitaire"):
            print_solitaire_rules()
        elif (command == "play solitaire"):
            play_solitaire()
        elif (command == "score solitaire"):
            print_solitaire_score()
        elif (command == "rules egyptian war"):
            print_egyptian_war_rules()
        elif (command == "play egyptian war"):
            play_egyptian_war()
        elif (command == "score egyptian war"):
            print_egyptian_war_score()
        elif (command == "rules blackjack"):
            print_blackjack_rules()
        elif (command == "play blackjack"):
            play_blackjack()
        elif (command == "score blackjack"):
            print_blackjack_score()
        elif (command == "rules aces up"):
            print_aces_up_rules()
        elif (command == "play aces up"):
            play_aces_up()
        elif (command == "score aces up"):
            print_aces_up_score()
        elif (command == "rules go fish"):
            print_go_fish_rules()
        elif (command == "play go fish"):
            play_go_fish()
        elif (command == "score go fish"):
            print_go_fish_score()
        elif (command == "end program"):
            playing = False
        else:
            print(Fore.RED + "\nThat is not a valid command.")

print(Fore.YELLOW + "Welcome to Brady Cason's card games.")
non_game_loop()
