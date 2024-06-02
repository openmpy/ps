n, m = map(int, input().split())
b = list(map(int, input().split()))

left, right = max(b), sum(b)
answer = 0

while left <= right:
  mid = (left + right) // 2

  blueray_num = 1
  remain = mid

  for i in b:
    if remain < i:
      blueray_num += 1
      remain = mid
    
    remain -= i

  if blueray_num <= m:
    answer = mid
    right = mid - 1
  else:
    left = mid + 1

print(answer)