"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B .
If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
"""
T = int(input())

for _ in range(T):
    a = int(input())
    A_num = set(list(map(int, input().split()))[:a])
    b = int(input())
    B_num = set(list(map(int, input().split()))[:b])

    print(A_num.issubset(B_num))

