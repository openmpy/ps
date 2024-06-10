import sys

# sys.stdin = open("input.txt", "r")

def sol(n):
    if n == 1:
        return '-'
    
    text = sol(n // 3)
    center = ' ' * (n // 3)

    return text + center + text

while True:
    try:
        n = int(sys.stdin.readline().strip())
        print(sol(3 ** n))
    except:
        break