from itertools import permutations

n = int(input())

t = []
for _ in range(n):
  t.append(list(map(str, input().split())))

answer = 0

for per in permutations(range(1, 10), 3):
  is_ok = True

  for score, strike, ball in t:
    real_strike = real_ball = 0

    for i in range(3):
      if str(per[i]) == score[i]:
        real_strike += 1
      elif str(per[i]) in score:
        real_ball += 1
    
    if int(strike) != real_strike or int(ball) != real_ball:
      is_ok = False
      break
  
  if is_ok:
    answer += 1

print(answer)