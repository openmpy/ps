def solution(n):
    a = -1

    if n ** 0.5 % 1 == 0:
        n2 = n ** 0.5 + 1
        a = n2 ** 2
        
    return a