l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()

choose = []
check = ['a', 'e', 'i', 'o', 'u']

def combination(index, level):
  if level == l:
    cnt, cnt2 = 0, 0
    for ch in choose:
      if ch in check:
        cnt += 1
      else:
        cnt2 += 1

    if cnt >= 1 and cnt2 >= 2:
      print(''.join(choose))

    return
  
  for i in range(index, c):
    choose.append(arr[i])
    combination(i + 1, level + 1)
    choose.pop()

combination(0, 0)
