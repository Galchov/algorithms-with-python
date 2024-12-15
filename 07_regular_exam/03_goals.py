"""
Input:
0, 1, 3, 2, 4, 6, 5
Output:
0 1 3 4 6
"""


def longest_increasing_subsequence(goals):
    n = len(goals)
    if n == 0:
        return []

    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if goals[i] >= goals[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_index = dp.index(max(dp))

    lis = []
    while max_index != -1:
        lis.append(goals[max_index])
        max_index = prev[max_index]

    lis.reverse()
    return lis


input_goals = input().strip()
goals = list(map(int, input_goals.split(", ")))

best_sequence = longest_increasing_subsequence(goals)
print(" ".join(map(str, best_sequence)))
