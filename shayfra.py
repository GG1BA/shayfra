import random

abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
numbers = "0123456789"
symbols = "!?@#$%^&*()-_+=/|\\,.:;'\"<>"

print("Shayfra alpha 4.1. Input \"help\" and press \"Enter\" to display help-menu."
      "\n=======================================================================================")


def abcGen(x):
    password = ""
    for i in range(0, x):
        password += random.choice(abc)
    return password

def numGen(x):
    password = ""
    for i in range(0, x):
        password += random.choice(numbers)
    return password

def symGen(x):
    password = ""
    for i in range(0, x):
        password += random.choice(symbols)
    return password

def passGen(x):
    password = ""
    for i in range(0, x):
        password += random.choice(abc+symbols+numbers)
    return password


def vernamEncrypt(key, word):
    if len(key) == len(word):
        binKey = []
        binWord = []
        code = ""
        for i in key:
            binKey.append(bin(ord(i))[2:])
        for i in word:
            binWord.append(bin(ord(i))[2:])
        for i in range(len(key)):
            code += str(int(binKey[i]) ^ int(binWord[i])) + " "
        return code
    else:
        return False

def vernamDecrypt(key, code):
    if len(key) == len(code):
        out = ""
        binKey = []
        for i in key:
            binKey.append(bin(ord(i))[2:])
        for i in range(len(code)):
            out += str(chr(int(str(int(code[i]) ^ int(binKey[i])), 2)))
        return out
    else:
        return False


while True:
    cmd = input("Enter the command: ")
    if cmd == "help":
        print("encrypt - encodes the string using the key."
              "\ndecrypt - decodes the code using the key."
              "\npassgen (x) - generates a hard password that contains letters, numbers and symbols."
              "\nnumgen (x) - generates a code that contains the symbols only."
              "\nsymgen (x) - generates a string of the symbols."
              "\nabcgen (x) - generates a password that contains letters the only."
              "\nquit or q - closes Shayfra."
              "\nWHERE:"
              "\n(x) - the length of the password.")
    elif cmd[0:7].lower() == "passgen":
        cmd = cmd.lower().split("passgen")
        try:
            x = int(cmd[1])
            print("Your password:", passGen(x))
        except ValueError:
            print("ERROR: enter the length."
                  "\nExamples:"
                  "\npassgen 13"
                  "\nnumgen 99"
                  "\nsymgen 1"
                  "\nabcgen 34")
    elif cmd[0:6].lower() == "abcgen":
        cmd = cmd.lower().split("abcgen")
        try:
            x = int(cmd[1])
            print("Your password:", abcGen(x))
        except ValueError:
            print("ERROR: enter the length."
                  "\nExamples:"
                  "\npassgen 13"
                  "\nnumgen 99"
                  "\nsymgen 1"
                  "\nabcgen 34")
    elif cmd[0:6].lower() == "numgen":
        cmd = cmd.lower().split("numgen")
        try:
            x = int(cmd[1])
            print("Your password:", numGen(x))
        except ValueError:
            print("ERROR: enter the length."
                  "\nExamples:"
                  "\npassgen 13"
                  "\nnumgen 99"
                  "\nsymgen 1"
                  "\nabcgen 34")
    elif cmd[0:6].lower() == "symgen":
        cmd = cmd.lower().split("symgen")
        try:
            x = int(cmd[1])
            print("Your password:", symGen(x))
        except ValueError:
            print("ERROR: enter the length."
                  "\nExamples:"
                  "\npassgen 13"
                  "\nnumgen 99"
                  "\nsymgen 1"
                  "\nabcgen 34")
    elif cmd[0:7].lower() == "encrypt":
        while True:
            key = input("Enter the key: ")
            if key == "":
                break
            else:
                while True:
                    word = input("Enter the string for encryption: ")
                    try:
                        if word == "":
                            break
                        elif vernamEncrypt(key, word):
                            print("Your code:", vernamEncrypt(key, word))
                            break
                        else:
                            print("ERROR: the length of the string must be equal to the length of the key.")
                            continue
                    except ValueError:
                        print("ValueError: please, try \"encrypt\" command again.")
                        break
                break
    elif cmd[0:7].lower() == "decrypt":
        while True:
            code = input("Enter the code for decryption: ")
            if code == "":
                break
            else:
                code = code.split()
                while True:
                    key = input("Enter the key: ")
                    try:
                        if key == "":
                            break
                        elif vernamDecrypt(key, code):
                            print("Your string:", vernamDecrypt(key, code))
                            break
                        else:
                            print("ERROR: the length of the code must be equal to the length of the key.")
                            continue
                    except ValueError:
                        print("ValueError: please, try \"decrypt\" command again.")
                        break
                break
    elif cmd == "q" or cmd == "quit":
        break
    else:
        print("ERROR: invalid command. Enter \"help\" to display the commands.")
    print("=======================================================================================")