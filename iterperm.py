from itertools import permutations

s, k = input().split()
#print(sorted(list(permutations(s, int(k)))))
for i in sorted(list(permutations(s, int(k)))):
    print("".join(i))