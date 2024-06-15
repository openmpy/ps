from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

for i in range(1, n + 1):
  comb = combinations(nums, i)
  for com in comb:
    if sum(com) == s:
      answer += 1

print(answer)