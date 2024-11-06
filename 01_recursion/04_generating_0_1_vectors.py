def generate01(idx, vector):

    # Base case
    if idx >= len(vector):
        print(*vector, sep='')
        return

    # Recursive call within the loop
    for num in range(2):
        vector[idx] = num
        generate01(idx + 1, vector)


n = int(input())
vector = [None] * n
generate01(0, vector)
