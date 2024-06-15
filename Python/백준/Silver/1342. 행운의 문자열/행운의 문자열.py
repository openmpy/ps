from itertools import permutations

s = input()

answer = 0

def factorial(n):
  if n == 0:
    return 1
  
  return n * factorial(n - 1)

for perm in permutations(s):
  is_ok = True

  for i in range(len(perm) - 1):
    if perm[i] == perm[i + 1]:
      is_ok = False
      break
  
  if is_ok == True:
    answer += 1

for i in range(ord('a'), ord('z') + 1):
  n = s.count(chr(i))

  answer //= factorial(n)

print(answer)