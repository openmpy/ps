check = [-1] * 26

s = input()

for i, c in enumerate(s):
    check[ord(c) - ord('a')] = s.find(c)

print(*check)