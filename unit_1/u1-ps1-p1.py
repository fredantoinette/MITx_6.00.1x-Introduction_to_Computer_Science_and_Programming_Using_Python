"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

# test
s = 'azcbobobegghakl'

num_vowels = 0
for letter in s:
    if letter in ('a', 'e', 'i', 'o', 'u'):
        num_vowels += 1
print("Number of vowels:", str(num_vowels))
