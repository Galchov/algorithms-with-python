# Dynamic solution
def calculate_binomial(n, k, memo):
    key = f'{n} {k}'
    if key in memo:
        return memo[key]

    if n == 0 or k == 0 or n == k:
        return 1

    result = calculate_binomial(n - 1, k - 1, memo) + calculate_binomial(n - 1, k, memo)
    memo[key] = result

    return result


def calc_binomial_recursion(n, k):
    if n == 0 or k == 0 or n == k:
        return 1

    return calc_binomial_recursion(n - 1, k - 1) + calc_binomial_recursion(n - 1, k)


n = int(input())
k = int(input())

print(calculate_binomial(n, k, {}))
# print(calc_binomial_recursion(n, k))
