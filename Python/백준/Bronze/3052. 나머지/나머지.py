check = [False] * 42

for _ in range(10):
    n = int(input())
    check[n % 42] = True

print(sum(check))