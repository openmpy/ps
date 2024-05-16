def solution(n):
    s = sorted(list(map(str, str(n))), reverse = True)
    a = ""

    for c in s:
        a += c
        
    return int(a)