"""
You are given a list of N lowercase English letters.
For a given integer K, you can select any K indices
 (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K
indices selected will contain the letter: 'a'.

Before I start I gotta talk about how we can find a probability of
anything:
Probability of something happening = number of ways the event can occur ÷ total number of outcomes
STEP-1: Find your event. In this case the event is the letters
STEP-2: Find all the outcomes. The total number of outcomes in this scenario is N letters
STEP-3: Find your desired outcome. Our desired outcome is at least 1 'a'
STEP-4: Do your calculation.
"""
from itertools import *

N = int(input())  # numbers of the letters
Letters = input().split()[:N]  # the letters
K = int(input()) # how many indices per tuple
a_pos = []
for id, c in enumerate(Letters):
    if c == 'a':
        a_pos.append(id + 1)

combination = list(combinations(range(1, N + 1), K))
print(round((len(set([y for x in a_pos for y in combination if x in y]))) / len(combination), 4))
