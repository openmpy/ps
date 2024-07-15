import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
q = int(input())

mistake = [0] * n

for i in range(1, n):
  if nums[i - 1] > nums[i]:
    mistake[i] = mistake[i - 1] + 1
  else:
    mistake[i] = mistake[i - 1]

for _ in range(q):
  x, y = map(int, input().split())
  print(mistake[y - 1] - mistake[x - 1])
