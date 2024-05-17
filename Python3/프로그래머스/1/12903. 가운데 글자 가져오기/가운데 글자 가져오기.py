def solution(s):
    l = len(s) // 2
    answer = ""

    if len(s) % 2 == 0:
        answer = s[l - 1 : l + 1]
    else:
        answer = s[l]
        
    return answer