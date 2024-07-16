n, k, b = map(int, input().split())

check = [0] * n

for _ in range(b):
  i = int(input())
  check[i - 1] = 1

psum = [0] * n
psum[0] = check[0]

for i in range(1, n):
  psum[i] = psum[i - 1] + check[i]

tsum = []

for i in range(n - k + 1):
  if i == 0:
    s = psum[i + k - 1]
  else:
    s = psum[i + k - 1] - psum[i - 1]

  tsum.append(s)

print(min(tsum))