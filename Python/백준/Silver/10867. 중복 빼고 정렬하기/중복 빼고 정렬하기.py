n = int(input())

nums = set(map(int, input().split()))

for num in sorted(nums):
  print(num, end=' ')