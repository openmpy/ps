n = int(input())
m = int(input())

arr = [[] for _ in range(n)]

for _ in range(m):
  x, y = list(map(int, input().split()))

  arr[x - 1].append(y - 1)
  arr[y - 1].append(x - 1)

# 친구 배열 채우기
friend = [0] * n
for i in arr[0]:
  friend[i] = 1

# 친구의 친구 배열 채우기
friend2 = [0] * n

for i in range(n):
  if friend[i] == 0:
    continue

  for j in arr[i]:
    if j != 0 and friend[j] == 0:
      friend2[j] = 1

print(sum(friend) + sum(friend2))