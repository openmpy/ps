n = int(input())

low = 0
high = 2 ** 32

ans = 0

while low <= high:
  mid = (low + high) // 2
  if mid ** 2 < n:
    low = mid + 1
  else:
    high = mid - 1
    ans = mid

print(ans)