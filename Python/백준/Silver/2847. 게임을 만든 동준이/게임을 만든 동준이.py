N = int(input())

answer = 0
score = []

for _ in range(N):
  score.append(int(input()))

m = score[-1]

for i in range(N - 2, -1, -1):
  if score[i] >= m:
    answer += score[i] - m + 1
    score[i] = m - 1
    m -= 1
  else:
    m = score[i]

print(answer)