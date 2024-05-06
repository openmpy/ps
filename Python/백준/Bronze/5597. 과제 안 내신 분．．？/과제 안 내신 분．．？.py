check = [False] * 30

for _ in range(28):
    n = int(input())
    check[n - 1] = True

for i, c in enumerate(check):
    if c == True:
        continue

    print(i + 1)