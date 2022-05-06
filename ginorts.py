"""
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:
    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.
"""

S = input('Give the string: ')

low = [i for i in S if i.islower()]
upper = [i for i in S if i.isupper()]
num = [i for i in S if i.isdigit()]
# print(f'lower case: {low}\nupper case: {upper}\nnumerical: {num}')
c = ""
for l in sorted(low):
    c += str(l)
for t in sorted(upper):
    c += str(t)
for n in sorted(list(map(int, sorted(num))), key=lambda x: x % 2 == 0):
    c += str(n)

print(c)
