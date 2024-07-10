import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

ans = -1

while left <= right:
  s = 0
  mid = (left + right) // 2

  for tree in trees:
    if tree > mid:
      s += tree - mid

  if s >= M:
    ans = mid
    left = mid + 1
  else:
    right = mid - 1

print(ans)