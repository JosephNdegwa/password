import email
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

        print("Please enter password")
        password = input()
        print("\n")

        print("Please enter your email")
        email = input()
        print("\n")


        handle = open("credential.txt","a")

        handle.write(username)
        handle.write(" ")
        handle.write(password)
        handle.write(" ")
        handle.write(email)
        handle.write("\n")


        handle.close()
        print("Your ccount has been created\n Would you like to explore more?(y/n)")
        response = input().lower()
        if response == 'y':
            generate_account()

        else:
            print("Get back to us to save a password for you!")

    elif answer == 'y':
        login()



def generate_account():
    print("Which account would you like to save a password for?")
    account_to_be_saved = input()
    print("Enter 'auto'- for an auto-generated password or 'mine'- to save your own password")
    choice = input()
    if choice == 'auto':
        reversed_account_name = account_to_be_saved[::-1]
        r = str(random.randint(0,50))
        password = reversed_account_name + r
        handle = open("account_and_password.txt","a")

        handle.write(account_to_be_saved)
        handle.write(" ")
        handle.write(password)
        handle.write(" ")


