n = int(input())
m = int(input())

arr = [[] for _ in range(n)]

for _ in range(m):
  x, y = list(map(int, input().split()))

  arr[x - 1].append(y - 1)
  arr[y - 1].append(x - 1)

cnt = [0] * n
cnt[0] = 1

while True:
  is_flag = False

  for i in range(n):
    if cnt[i] == 0:
      continue

    for j in arr[i]:
      if cnt[j] == 0:
        cnt[j] = 1
        is_flag = True

  if not is_flag:
    break

answer = 0
for i in range(1, n):
  if cnt[i] == 1:
    answer += 1

print(answer)