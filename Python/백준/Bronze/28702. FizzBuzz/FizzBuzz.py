a = input()
b = input()
c = input()

answer = 0

if a.isnumeric():
  answer = int(a) + 3
if b.isnumeric():
  answer = int(b) + 2
if c.isnumeric():
  answer = int(c) + 1

if answer % 3 == 0 and answer % 5 == 0:
  print('FizzBuzz')
elif answer % 3 == 0 and answer % 5 != 0:
  print('Fizz')
elif answer % 3 != 0 and answer % 5 == 0:
  print('Buzz')
else:
  print(answer)