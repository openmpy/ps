def solution(n, m, section):
    answer = 0
    index = 0

    for i in section:
        if i >= index:
            index = i + m
            answer += 1
            
    return answer