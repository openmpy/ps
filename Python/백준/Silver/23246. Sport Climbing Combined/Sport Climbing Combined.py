n = int(input())

arr = []
rank = []

for _ in range(n):
  score = list(map(int, input().split()))

  m = score[1] * score[2] * score[3]
  s = sum(score[1:])
  n = score[0]

  arr.append([m, s, n])

rank = sorted(arr)
for i in range(3):
  print(rank[i][2], end = ' ')