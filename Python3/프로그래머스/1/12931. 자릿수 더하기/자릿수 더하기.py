def solution(n):
    s = str(n)
    return sum(ord(c) - ord('0') for c in s)