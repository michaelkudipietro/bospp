"""Collatz Sequence, by Al Sweigart
Generates numbers for the Collatz sequence, given a starting number."""

import sys, time

print('''Collatz Sequence, or, the 3n+1 Problem
      
      The Collatz sequence is a sequence of numbers produced from a starting
      number n, following three rules:

      1) if n is even, the next number n is n/2.
      2) if n is odd, the next number n is 3n+1.
      3) if n is 1, stop. Otherwise repeat.

      It is generally thought, but so far not mathematically proven, that
      every starting number eventually terminates at 1.
      ''')

print('Enter a starting number (greater than 0) or QUIT:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()

print()
n=int(response)
iterations=0
print(n,end='',flush=True)
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    
    print(', '+str(n),end='',flush=True)
    time.sleep(0.1)
    iterations+=1
print()
print("It took ", iterations, " iterations to reach a value of n=1 in this sequence.\n\n")

