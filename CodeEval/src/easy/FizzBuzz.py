'''
Created on Jan 21, 2015

@author: Puneeth U Bharadwaj

FIZZ BUZZ

CHALLENGE DESCRIPTION:
Players generally sit in a circle. The first player says the number “1”, and each player says next number in turn.
However, any number divisible by X (for example, three) is replaced by the word fizz, and any divisible by Y (for example, five) by the word buzz.
Numbers divisible by both become fizz buzz. A player who hesitates, or makes a mistake is eliminated from the game.

Write a program that prints out the final series of numbers where those divisible by X, Y and both are replaced by
“F” for fizz, “B” for buzz and “FB” for fizz buzz.

INPUT SAMPLE:
Your program should accept a file as its first argument.
The file contains multiple separated lines; each line contains 3 numbers that are space delimited.
The first number is the first divider (X), the second number is the second divider (Y), and the third number is how far you should count (N).
You may assume that the input file is formatted correctly and the numbers are valid positive integers.

For example:
1 3 5 10
2 2 7 15

OUTPUT SAMPLE:
Print out the series 1 through N replacing numbers divisible by X with “F”, numbers divisible by Y with “B” and numbers divisible by both with “FB”.
Since the input file contains multiple sets of values, your output should print out one line per set.
Ensure that there are no trailing empty spaces in each line you print.

1 1 2 F 4 B F 7 8 F B
2 1 F 3 F 5 F B F 9 F 11 F 13 FB 15

CONSTRAINTS:
The number of test cases ≤ 20
"X" is in range [1, 20]
"Y" is in range [1, 20]
"N" is in range [21, 100]
'''

import sys

xynlist = []
test_cases = open('C:/input.txt', 'r')
for test in test_cases:
    xyn = str(test)
    xynlist = xyn.split()
    X = int(xynlist[0])
    Y = int(xynlist[1])
    N = int(xynlist[2])
    
    op = ' '
    i = 1
    while i <= N :
        if (i%X==0 and i%Y==0):
            op = op + 'FB' + ' '
        elif(i%X==0):
            op = op + 'F' + ' '
        elif(i%Y==0):
            op = op + 'B' + ' '
        else:
            op = op + str(i) + ' '
            
        i = i + 1
    
    print (op.strip())
    op = ' '

test_cases.close()