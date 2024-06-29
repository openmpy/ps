n = int(input())

l = len(str(n))
s = 0

for i in range(1, l):
  s += i * ((10 ** i - 1) - (10 ** (i - 1)) + 1)
s += (n - (10 ** (l - 1)) + 1) * l

print(s)