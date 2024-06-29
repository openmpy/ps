A, B, C, M = map(int, input().split())

p = 0
w = 0

for i in range(24):
  if p + A > M:
    p = max(0, p - C)
  else:
    p += A
    w += B

print(w)