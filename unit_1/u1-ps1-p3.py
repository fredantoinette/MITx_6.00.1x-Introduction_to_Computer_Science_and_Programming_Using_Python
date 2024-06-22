"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""

# test
s = "azcbobobegghakl"
s = "abcbcd"


s1 = ""
s2 = ""

for letter in s:
    if s2 == "" and s1 == "":
        s2 = letter
        s1 = letter
    elif letter >= s2[-1]:
        s2 += letter
        if len(s2) > len(s1):
            s1 = s2[:]
    else:
        s2 = ""
        s2 += letter
        
print("Longest substring in alphabetical order is:", s1)
