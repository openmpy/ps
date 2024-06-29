from itertools import combinations

n, m = map(int, input().split())

for com in combinations(range(1, n + 1), m):
  lst = list(map(str, com))
  print(' '.join(lst))