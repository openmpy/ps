import sys

# sys.stdin = open("input.txt", "r")

while True:
    text = input()

    if text == '.':
        break

    stack = []
    isFlag = False

    for c in text:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif (c == ']' or c == ')') and (not stack or stack.pop() != c):
            isFlag = True
            break
    
    if stack:
        isFlag = True

    print('no' if isFlag else 'yes')