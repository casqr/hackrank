"""
You have to generate a list of the first N fibonacci numbers,
0 being the first number.
Then, apply the map function and a lambda expression
to cube each fibonacci number and print the list. """

cube = lambda x: x ** 3  # complete the lambda function

def fibonacci(n):
    fib_num = []
    for i in range(n):
        # fib_num.append(fib_num[i] + fib_num[i + 1])
        if len(fib_num) <= 1:
            fib_num.append(i)
        else:
            fib_num.append(fib_num[i - 1] + fib_num[i - 2])
    # return fib_num[:n]
    return fib_num
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
