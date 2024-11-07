def recursive_fibonacci(number):
    if number <= 1:
        return 1
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)


def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


n = int(input())
# print(recursive_fibonacci(n))
print(iterative_fib(n))
