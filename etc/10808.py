import sys
from string import ascii_lowercase
S = sys.stdin.readline()
alphabet = list(ascii_lowercase)
for alpha in alphabet:
    print(S.count(alpha),end = ' ')
