n = int(input())
g = list(map(int, input().split()))
m = int(input())

if sum(g) <= m:
  print(max(g))
else:
  left, right = 0, max(g)
  answer = 0

  while left <= right:
    s = 0
    mid = (left + right) // 2

    for i in g:
      s += min(i, mid)
    
    if s <= m:
      answer = mid
      left = mid + 1
    else:
      right = mid - 1
  
  print(answer)