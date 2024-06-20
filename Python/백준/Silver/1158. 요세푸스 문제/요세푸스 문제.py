from collections import deque

n, k = map(int, input().split())

arr = deque(i for i in range(1, n + 1))
tmp = []

while arr:
  for _ in range(k - 1):
    arr.append(arr.popleft())
  tmp.append(arr.popleft())

print('<' + ', '.join(map(str, tmp)) + '>')