import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  arr = []

  for _ in range(N):
    s, m = map(int, input().split())
    arr.append((s, m))

  arr.sort()

  answer = 0
  r = 1e9

  for i in arr:
    if i[1] < r:
      r = i[1]
      answer += 1

  print(answer)
