n = int(input())

money = [500, 100, 50, 10, 5, 1]

m = 1000 - n
answer = 0

for i in money:
  answer += m // i
  m -= (m // i) * i

print(answer)