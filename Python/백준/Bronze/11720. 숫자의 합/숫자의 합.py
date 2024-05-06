import sys

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().strip())
m = sys.stdin.readline().strip()

sum = 0
for i in range(len(m)):
    sum += int(m[i])

print(sum)