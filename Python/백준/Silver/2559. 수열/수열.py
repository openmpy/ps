n, k = map(int, input().split())
nums = list(map(int, input().split()))

psum = [0] * n
psum[0] = nums[0]

for i in range(1, n):
  psum[i] = psum[i - 1] + nums[i]

tsum = []

for i in range(n - k + 1):
  s = 0

  if i == 0:
    s = psum[i + k - 1]
  else:
    s = psum[i + k - 1] - psum[i - 1]

  tsum.append(s)

print(max(tsum))