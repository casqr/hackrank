"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read
more about this function, Check this out . You are given a string S. Suppose a character 'c' occurs consecutively X
times in the string. Replace these consecutive occurrences of the character 'c'  with (X, c)
in the string.
 """
from itertools import groupby

S = input()
the_list = [(len(list(x)), int(c)) for c, x in groupby(S)]
print(*the_list)





