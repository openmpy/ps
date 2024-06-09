N, K = map(int, input().split())

money = []
answer = 0

for _ in range(N):
  money.append(int(input()))

for i in range(len(money) - 1, -1, -1):
  if money[i] <= K:
    answer += K // money[i]
    K %= money[i]

print(answer)