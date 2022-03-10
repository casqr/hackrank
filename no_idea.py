"""
 There is an array of integers.
 There are also 2 disjoint sets,A and B, each containing integers.
 You like all the integers in set A and dislike all the integers in set B.
 Your initial happiness is 0.
 For each i integer in the array, if i in A, you add 1 to your happiness.
 If i in B, you add -1 to your happiness.
 Otherwise, your happiness does not change.
 Output your final happiness at the end.

 Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
"""
n, m = list(map(int, input().split()))
n_int = list(map(int, input().split()))
n_num = n_int[:n]
a_num = list(map(int, input().split()))
b_num = list(map(int, input().split()))
A = set(a_num[:m])
B = set(b_num[:m])
total_hap = 0
for i in n_num:
    if i in A:
        total_hap += 1
    elif i in B:
        total_hap -= 1

print(total_hap)