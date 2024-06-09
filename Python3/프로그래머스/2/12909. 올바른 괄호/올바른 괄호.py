def solution(s):
    answer = True
    stx = []

    for c in s:
        if c == '(':
            stx.append(')')
        else:
            if len(stx) == 0:
                answer = False
                break

            if stx.pop() != c:
                answer = False
                break
                
    if len(stx) != 0:
        answer = False
        
    return answer