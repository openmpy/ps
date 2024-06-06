N, M = map(int, input().split())

numbers = list(map(int, input().split()))
answer = 0

left, right = 0, 0
s = numbers[0]

answer = 0

while True:
  if s == M:
    answer += 1
    
  if s >= M:
    left += 1
    s -= numbers[left - 1]
  else:
    if right == N - 1:
      break

    right += 1
    s += numbers[right]

print(answer)