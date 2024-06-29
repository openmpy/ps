s = input()

lst = s.split('.')
answer = []

for l in lst:
  if len(l) % 2 == 1:
    answer.clear()
    answer.append('-1')
    break
  
  a = len(l) // 4
  b = 0

  if a == 0:
    b = len(l) // 2
  else:
    b = (len(l) - (4 * a)) // 2

  answer.append('AAAA' * a + 'BB' * b)

print('.'.join(answer))