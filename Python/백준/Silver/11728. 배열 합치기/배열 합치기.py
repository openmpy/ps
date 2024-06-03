import sys

input = sys.stdin.readline

A, B = map(int, input().split())
arr = []

for _ in range(2):
  numbers = list(map(int, input().split()))

  for number in numbers:
    arr.append(number)

arr.sort()

for i in arr:
  print(i, end=' ')