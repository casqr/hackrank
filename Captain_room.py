"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel. The tourists consist of: → A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.
The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of
the tourists. The room numbers will appear K times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.
"""
from collections import Counter

K = int(input())
Num = list(map(int, input().split()))
u_num = Counter(Num)
for x, y in u_num.items():
    if y != K:
        print(x)

# You can also use this other method but it's slower:
"""
K = int(input())
Num = list(map(int, input().split()))

n_um = {}
for l in Num:
    if l in n_um:
        n_um[l]+=1
    else:
        n_um[l] = 1
    
for x, y in n_um.items():
    if y != K:
        print(x)
"""
