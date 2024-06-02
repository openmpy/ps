import sys
from collections import deque

n = int(input())

arr = deque([])
answer = []

for i in range(n):
  text = sys.stdin.readline().split()
  string = text[0]

  if string == "push":
    number = int(text[1])
    arr.append(number)
  elif string == "pop":
    if len(arr) == 0:
      answer.append(-1)
    else:
      answer.append(arr.popleft())
  elif string == "size":
    answer.append(len(arr))
  elif string == "empty":
    if len(arr) == 0:
      answer.append(1)
    else:
      answer.append(0)
  elif string == "front":
    if len(arr) == 0:
      answer.append(-1)
    else:
      answer.append(arr[0])
  elif string == "back":
    if len(arr) == 0:
      answer.append(-1)
    else:
      answer.append(arr[-1])

for i in answer:
  print(i)