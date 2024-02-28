#Directions:
#exectute "Card_Games.py" in Geany.
#open a cmd window and type "python"
#then copy this code into it and hit enter twice.
#quickly click on the running "Card_Games.py" window and watch as egytian war is simulated
import pyautogui as py
import time

for i in range(0,20):
    time.sleep(5)
    py.write('play egyptian war\n', interval=0.1)
    time.sleep(1)
    py.write('simulate\n', interval=0.1)
    
