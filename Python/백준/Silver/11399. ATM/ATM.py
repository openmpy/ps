N = int(input())
P = list(map(int, input().split()))

P.sort()
answer = 0

for i in range(len(P)):
  s = 0

  for j in range(i + 1):
    s += P[j]

  answer += s

print(answer)