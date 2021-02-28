import random
import string
import time
import ctypes
import os
score = 0
botscore = 0
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Rock Paper Scissors")
    rps = ['Rock', 'Paper', 'Scissors']
    player1 = input("Enter your choice: ")
    ai1 = random.choice(rps)
    print("The Bot Chose: " + ai1)
    if player1 == 'Rock':
        if ai1 == 'Rock':
            print("It's a tie!")
        if ai1 == 'Paper':
            print("You lost against Paper with Rock!")
        if ai1 == 'Scissors':
            print("You won against Scissors with rock!")
    if player1 == 'Scissors':
        if ai1 == 'Rock':
            print("You lost against Rock with Scissors!")
        if ai1 == 'Paper':
            print("You won against Paper with Scissors")
        if ai1 == 'Scissors':
            print("It's a tie!")
    if player1 == 'Paper':
        if ai1 == 'Rock':
            print("You won against Rock with Paper!")
        if ai1 == 'Paper':
            print("It's a tie!")
        if ai1 == 'Scissors':
            print("You lost against Scissors with Paper!")
    time.sleep(5)
    cls()
while True:
    main()