"""
You have a non-empty set s, and you have to execute N commands given N in lines.
The commands will be pop, remove and discard.
"""
n = int(input())
s = set(filter(lambda x: x <= 9, list(map(int, input().split()))[:n]))
print(s)
N = int(input())
for i in range(N):
    com = input().split()
    if com[0] == 'pop':
        if len(s) != 0:
            s.pop()
    elif com[0] == 'remove':
        try:
            s.remove(int(com[1]))
        except KeyError:
            continue
    elif com[0] == 'discard':
        s.discard(int(com[1]))
print(sum(s))