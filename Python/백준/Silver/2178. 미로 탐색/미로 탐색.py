from collections import deque

n, m = map(int, input().split())

visit = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dq = deque([(0, 0)])
visit[0][0] = True
dist[0][0] = 0

rooms = []

for _ in range(n):
  rooms.append(input())

while len(dq) != 0:
  r, c = dq.popleft()

  if r > 0 and rooms[r - 1][c] == '1' and visit[r - 1][c] == False:
    dq.append((r - 1, c))
    visit[r - 1][c] = True
    dist[r - 1][c] = dist[r][c] + 1

  if r < n - 1 and rooms[r + 1][c] == '1' and visit[r + 1][c] == False:
    dq.append((r + 1, c))
    visit[r + 1][c] = True
    dist[r + 1][c] = dist[r][c] + 1

  if c > 0 and rooms[r][c - 1] == '1' and visit[r][c - 1] == False:
    dq.append((r, c - 1))
    visit[r][c - 1] = True
    dist[r][c - 1] = dist[r][c] + 1

  if c < m - 1 and rooms[r][c + 1] == '1' and visit[r][c + 1] == False:
    dq.append((r, c + 1))
    visit[r][c + 1] = True
    dist[r][c + 1] = dist[r][c] + 1

print(dist[n - 1][m - 1] + 1)