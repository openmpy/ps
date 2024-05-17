def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        n = int(t[i : i + len(p)])
        m = int(p)

        if n <= m:
            answer += 1
            
    return answer