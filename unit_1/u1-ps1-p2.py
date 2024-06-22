"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

# test
s = 'azcbobobegghakl'

num_times_bob = 0
for start in range(len(s)):
    if s[start:(start+3)] == 'bob':
        num_times_bob += 1
print("Number of times bob occurs is:", str(num_times_bob))
