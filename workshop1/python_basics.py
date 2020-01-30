"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import numpy as np
import random as rand
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    num = rand.randint(1, 9)
    x = '\0'
    while(x != exit):
        x = input("Please enter a number between 1 and 9, or type \'exit\' to quit: ")
        if(x == "exit"):
            print("Goodbye!")
            return None
        if(not x.isdigit()):
            print("Invalid input.")
        elif(int(x) not in range(1, 9)):
            print("Invalid input.")
        elif(int(x) > num):
            print("Your guess was too high.")
        elif(int(x) < num):
            print("Your guess was too low.")
        elif(int(x) == num):
            print("Your guess was correct! New number generated.")
            num = rand.randint(1, 9)
    

    

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    for i in range(int(np.ceil(np.float64(len(string))/2))):
        if string[i] != string[-i-1]:
            print("False")
            return None
    print("True")
        

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f = open(filename, 'w')
    encodedBytes = base64.b64encode(username.encode("utf-8"))
    encodedUsername = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(password.encode("utf-8"))
    encodedPassword = str(encodedBytes, "utf-8")
    L = [encodedUsername + '\n', encodedPassword + '\n']
    f.writelines(L)
    f.close()
    return None

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, 'r')
    L = f.readlines()
    print(str(base64.b64decode(L[0]), "utf-8"))
    print(str(base64.b64decode(L[1]), "utf-8"))
    f.close()
    if(password != None):
        f = open(filename, 'w')
        L[1] = str(base64.b64encode(password.encode("utf-8")), "utf-8")
        f.writelines(L)
        f.close()
    return None

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
