n, m = map(int, input().split())
position = list(map(int, input().split()))

answer = 0

neg = []
pos = []

for x in position:
  if x < 0:
    neg.append(-x)
  else:
    pos.append(x)

neg.sort(reverse=True)
pos.sort(reverse=True)

dists = []

for i in neg[::m]:
  dists.append(i)

for i in pos[::m]:
  dists.append(i)

for d in dists:
  if max(dists) == d:
    answer += d
  else:
    answer += d * 2

print(answer)