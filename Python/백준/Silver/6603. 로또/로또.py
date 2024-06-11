n = 0
choose = []

def combination(lst, index, level):
  if level == 6:
    print(*choose)
    return
  
  for i in range(index, n):
    choose.append(lst[i])
    combination(lst, i + 1, level + 1)
    choose.pop()

while True:
  t = list(map(int, input().split()))
  if t[0] == 0:
    break

  n = t[0]
  arr = t[1:]

  combination(arr, 0, 0)
  choose.clear()
  print()