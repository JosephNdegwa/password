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


        handle = open("credentials.txt","a")

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


