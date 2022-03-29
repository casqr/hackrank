"""
You are given a spreadsheet that contains a list of N
athletes and their details (such as age, height, weight and so on).
You are required to sort the data based on the Kth attribute and print the final resulting table.
"""
from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=itemgetter(k)):
        print(*i)
