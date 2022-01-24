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
    print("Please enter 'auto'- for an auto-generated password or 'mine'- to save your own password")
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



        handle.close()
        print(f"Password to your new {account_to_be_saved} account is {password} and has been saved and copied, you can paste it anywhere in your laptop")
        pyperclip.copy(password)
    else:
        print("Type your password")
        password = input()
        pyperclip.copy(password)

        print(f"Password to your new {account_to_be_saved} account is {password} and has been saved and copied, you can paste it anywhere in your laptop.")



def login():
    print("Please enter your username")
    username = input()
    print("\n")
    print("Please enter your password")
    password = input()
    print("\n")
    print("Please enter your email")
    email = input()
    for line in open("credential.txt", "r").readlines():
            myVar = line.split()
            if username == myVar[0] and password == myVar[1]:
                print("login successful")
                print("Would you like to explore more on Password?(y/n)")
                jibu = input()
                if jibu == 'y':
                    generate_account()
                else:
                    print("Get back to us to save a password for you!")


                return True
            else:
                print("Forgot your password ?(y/n)")
                response = input().lower()
                if response == 'y':
                    print("Please enter your username")
                    username = input()
                    for line in open("credential.txt", "r").readlines():
                        my_file = line.split()

                        to_be_printed = my_file[1]
                        username1 = my_file[0]
                        if username == username1:
                            print(f"your password is {to_be_printed}")
                        else:
                           
                            login()
                           
                else:
                    print("Please try again")

                    login()








class User:

    """
    Class that generates new instances of Users
    """
    User_list = []

    def __init__(self,username,password,email):

     

        self.username = username
        self.password = password
        self.email = email


class credential:

    """
    Class that generates new instances of Users
    """
    User_list = []

    def __init__(self,account,password,):

      

        self.account = account
        self.password = password



    all()

