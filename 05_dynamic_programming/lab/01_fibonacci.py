def calc_fib(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)

    memo[n] = result

    return memo[n]


n = int(input())

print(calc_fib(n, {}))
