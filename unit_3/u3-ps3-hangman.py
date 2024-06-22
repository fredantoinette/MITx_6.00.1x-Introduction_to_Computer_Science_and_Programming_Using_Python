"""
For this problem, you will implement a variation of the classic wordgame 
Hangman. In this problem, the second player will always be the computer, who 
will be picking a word at random.

In this problem, you will implement a function, called hangman, that will 
start up and carry out an interactive Hangman game between a player and the 
computer. Before we get to this function, we'll first implement a few helper 
functions to get you going.

For this problem, you will need the code files ps3_hangman.py and words.txt. 
Right-click on each and hit "Save Link As". Be sure to save them in same 
directory. Open and run the file ps3_hangman.py without making any 
modifications to it, in order to ensure that everything is set up correctly. 

The file ps3_hangman.py has a number of already implemented functions you can 
use while writing up your solution. You should read and understand how to use 
each helper function by reading the docstrings.

You will want to do all of your coding for this problem within this file as 
well because you will be writing a program that depends on each function you 
write.

Requirements
Here are the requirements for your game:
1. The computer must select a word at random from the list of available words 
that was provided in words.txt. The functions for loading the word list and 
selecting a random word have already been provided for you in ps3_hangman.py.
2. The game must be interactive; the flow of the game should go as follows:
- At the start of the game, let the user know how many letters the computer's 
word contains.
- Ask the user to supply one guess (i.e. letter) per round.
- The user should receive feedback immediately after each guess about whether 
their guess appears in the computer's word.
- After each round, you should also display to the user the partially guessed 
word so far, as well as letters that the user has not yet guessed.
3. Some additional rules of the game:
- A user is allowed 8 guesses. Make sure to remind the user of how many 
guesses s/he has left after each round. Assume that players will only ever 
submit one character at a time (A-Z).
- A user loses a guess only when s/he guesses incorrectly.
- If the user guesses the same letter twice, do not take away a guess - 
instead, print a message letting them know they've already guessed that letter 
and ask them to try again.
- The game should end when the user constructs the full word or runs out of 
guesses. If the player runs out of guesses (s/he "loses"), reveal the word to 
the user when the game ends.
"""


# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = True
    for l in secretWord:
        if l not in lettersGuessed:
            result = False
    return result

# test
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for l in secretWord:
        if l in lettersGuessed:
            result += l
        else:
            result += ' _ '
    return result

# test
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    letters = string.ascii_lowercase
    result = ''
    for l in letters:
        if l not in lettersGuessed:
            result += l
    return result

# test
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print("-------------")
    num_guesses = 8
    letters_guessed = []
    letter_input = ""
    while num_guesses > 0 and isWordGuessed(secretWord, letters_guessed) is False:
        available_letters = getAvailableLetters(letters_guessed).replace(letter_input, "")
        print("You have", num_guesses, "guess(es) left.")
        print("Available letters:", available_letters)
        letter_input = input("Please guess a letter: ").lower()
        letters_guessed.append(letter_input)
        if letter_input not in available_letters:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, letters_guessed))
        elif letter_input in secretWord:
            print("Good guess:", getGuessedWord(secretWord, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, letters_guessed))
            num_guesses -= 1
        print("-------------")
    if isWordGuessed(secretWord, letters_guessed) is True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord + ".")
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = "c" # testing if we can correctly guess a short word
#secretWord = "zzz" # testing if we can correctly fill in repeat letters
#secretWord = "c" # testing if we can incorrectly guess a short word
#secretWord = "sea" # testing if we handle repeat correct guesses
#secretWord = "y" # testing if we handle repeat incorrect guesses
hangman(secretWord)
