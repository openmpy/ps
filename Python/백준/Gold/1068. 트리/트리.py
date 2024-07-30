n = int(input())
parent = list(map(int, input().split()))
r = int(input())

# 루트 노드 찾기
for i in range(n):
  if parent[i] == -1:
    root = i
    break

# 사라지는 노드들 색칠
black = [0] * n
for i in range(n):
  u = i

  while True:
    if u == r:
      black[i] = 1
      break

    if u == root:
      break
  
    u = parent[u]

# 자식이 있는 노드들 색칠
red = [0] * n
for i in range(n):
  if black[i] == 1:
    continue

  if i == root:
    continue

  red[parent[i]] = 1

count = 0
for i in range(n):
  if black[i] == 0 and red[i] == 0:
    count += 1

print(count)
