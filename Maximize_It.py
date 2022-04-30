"""
You are given a function f(X)=X^2 You are also given K lists. Te ith list consists of Ni  elements. You have to
pick one element from each list so that the value from the equations below is maximized: S = (f(X1)+f(x2) + ....+ f(
xk))%M Xi denotes the element picked from the ith list. Find the maximized value Smax obtained. % denotes the modulo
operator. Note that you need to take exactly one element from each list, not necessarily the largest element. You add
the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain,
will be the answer to the problem.
"""
from itertools import product

K, M = map(int, input().split())
T = []

for i in range(K):
    N = list(map(int, input().split()))
    T.append(N[1:])
    assert len(T[i]) == N[0]

S_max = 0
L_max = None

for l in product(*T):
    s = sum([x ** 2 for x in l]) % M

    if s > S_max:
        S_max = s
        L_max = l
print(S_max)
