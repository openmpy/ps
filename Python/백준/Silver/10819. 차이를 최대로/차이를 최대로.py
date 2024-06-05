from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

answer = 0

for a in permutations(A, N):
  diff_sum = 0
  for i in range(N - 1):
    diff_sum += abs(a[i] - a[i + 1])

  answer = max(answer, diff_sum)

print(answer)