import time

def fib_naiveRecirsion(n):
    if n <= 1:
        return n
    return fib_naiveRecirsion(n - 1) + fib_naiveRecirsion(n - 2)

def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def time_measure(func, n):
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    return end - start

def __main__():
    # print('Enter your number:', end=' ')
    # n = int(input())
    # print(f'Recursive method: {fib_naiveRecirsion(n)}')
    # print(f'Iterative method: {fib_iterative(n)}')

    nums = [10, 20, 30, 40, 50]

    recursion_res = []
    iterative_res = []

    for n in nums:
        if n <= 40:
            t_recursive = time_measure(fib_naiveRecirsion, n)
        else:
            t_recursive = None

        t_iterative = time_measure(fib_iterative, n)

        recursion_res.append(t_recursive)
        iterative_res.append(t_iterative)

    print(f'Recursive method: {recursion_res}')
    print(f'Iterative method: {iterative_res}')


if __name__ == '__main__':
    __main__()
