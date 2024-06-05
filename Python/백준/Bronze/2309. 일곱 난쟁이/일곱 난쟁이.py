p = []
f = [0, 0]

for _ in range(9):
  p.append(int(input()))

for i in range(0, 8):
  for j in range(i + 1, 9):
    if p[i] + p[j] == sum(p) - 100:
      f[0], f[1] = p[i], p[j]
      break

p.remove(f[0])
p.remove(f[1])
p.sort()

for i in p:
  print(i)