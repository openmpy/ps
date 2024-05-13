n = int(input())
cnt = 0

for i in range(1, n):
    for j in range(i + 2, n):
        c = n - (i + j)

        if c % 2 == 1 or c <= 0:
            continue

        cnt += 1

print(cnt)