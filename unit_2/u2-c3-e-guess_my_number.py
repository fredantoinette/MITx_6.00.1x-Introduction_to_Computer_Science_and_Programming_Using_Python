"""
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!
"""

print("Please think of a number between 0 and 100!")

low = 0
high = 100
g = int((high + low) / 2)

while True:
    print("Is your secret number", str(g) + "?")
    print("Enter 'h' to indicate the guess is too high.", end = " ")
    print("Enter 'l' to indicate the guess is too low.", end = " ")
    print("Enter 'c' to indicate I guessed correctly.", end = " ")
    i = input("")
    if i == "h":
        high = g
    elif i == "l":
        low = g
    elif i == "c":
        print("Game over. Your secret number was:", str(g))
        break
    else:
        print("Sorry I did not understand your input.")
    g = int((high + low) / 2)
