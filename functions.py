import random

def ask_options():
    psw_lenght = 8
    options = ["y","y","y","y"]
    while True:
        try:
            psw_lenght = int(input("Introduce your desired password length (integer value): "))
            break
        except ValueError:
            print("You need to put an integer.")
        except TypeError:
            print("You need to put an integer.")

    choice = input("Do you want to modify your password generation settings? (Default are lowercase + capital + numbers + symbols)(Y/n): ").lower()
    if choice == "yes" | choice == "y":
            options[0] = input("Want lowercase letters in your password? (Y/n):").lower()
            options[1] = input("Want capital letters in your password? (Y/n)").lower()
            options[2] = input("Want numbers in your password? (Y/n): ").lower()
            options[3] = input("Want symbols in your password? (Y/n): ").lower()
    return psw_lenght,options

def generate_password():
    capital_letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnñopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "'-!\"#$%&()*,./:;?@[]^_`{|}~+<=>"
    
    psw_len,opts = ask_options()
    
    psw_builder = ""
    
    if opts[0] == "yes" | opts[0] == "y":
        psw_builder += capital_letters
    if opts[1] == "yes" | opts[1] == "y":
        psw_builder += lowercase_letters
    if opts[2] == "yes" | opts[2] == "y":
        psw_builder += numbers
    if opts[3] == "yes" | opts[3] == "y":
        psw_builder += symbols

    password = "".join(random.sample(psw_builder,psw_len))
    print(password)