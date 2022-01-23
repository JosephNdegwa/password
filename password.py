from multiprocessing.connection import answer_challenge
import random
import pyperclip

def all():
    print("Do you have an existing account?(y/n)")
    answer = input().lower()

    if answer == 'n':
        print("Please enter your name:")
        username = input()
        print("\n")
        
