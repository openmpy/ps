T = int(input())

arr = list(map(int, input().split()))
C, P = map(int, input().split())

s = 0

for i in arr:
  if i % C == 0:
    s += i // C
  else:
    s += i // C + 1

print(s)
print(T // P, T - (T // P * P))
