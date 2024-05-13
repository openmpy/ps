n = int(input())

for _ in range(n):
    num = int(input())

    isCheck = False
    for i in range(2, 1_000_000):
        if num % i == 0:
            isCheck = True
            break
    
    print("NO" if isCheck else "YES")