import re
import string

print()
def choice():
    choicevar = input("would you like to encrypt or decrypt: ")
    if choicevar == "encrypt":
        encrypt()
    elif choicevar == "decrypt":
        decrypt()
    else:
        print("Invalid input-Try Again!")
        print()
        choice()

def encrypt():
    while True:
        try:
            shift = int(input("what would you like your shift to be: "))
        except ValueError:
            print()
            print("Invalid input-Try Again!")
            print()
            continue
        else:
            break
    plain_text = input("what word(s) would you like to have encrypted or decrypted using a cesar shift: ")
    alphabet = string.ascii_lowercase
    print()
    #print(alphabet)
    shifted = alphabet[shift:] + alphabet[0:shift]
    #print(shifted)
    translated = str.maketrans(alphabet,shifted)
    encrypted = plain_text.translate(translated)
    print(encrypted)
    print()
    while True:
        anothachoice = input('would you like to encrypt another word or decrypt (input either "encrypt" or "decrypt"): ')
        if anothachoice == "encrypt":
            print()
            print("loading new encryption algorithm...")
            print()
            encrypt()
        elif anothachoice == "decrypt":
            print()
            decrypt()
        else:
            print("Invalid input-Try Again!")

def decrypt():
    while True:
        try:
            shift = int(input("what is the shift to your cipher: "))
        except ValueError:
            print()
            print("Invalid input-Try Again!")
            print()
            continue
        else:
            break
    plain_text = input("what word(s) would you like to have encrypted or decrypted using a cesar shift: ")
    shift = 26 - shift
    alphabet = string.ascii_lowercase
    print()
    # print(alphabet)
    shifted = alphabet[shift:] + alphabet[0:shift]
    # print(shifted)
    translated = str.maketrans(alphabet, shifted)
    encrypted = plain_text.translate(translated)
    print(encrypted)
    print()
    while True:
        anothachoice = input(
            'would you like to encrypt another word or decrypt (input either "encrypt" or "decrypt"): ')
        if anothachoice == "encrypt":
            print()
            print("loading new encryption algorithm...")
            print()
            encrypt()
        elif anothachoice == "decrypt":
            print()
            decrypt()
        else:
            print("Invalid input-Try Again!")

choice()
#encrypt()
#decrypt()
