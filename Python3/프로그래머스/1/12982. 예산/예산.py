def solution(d, budget):
    d = sorted(d)
    answer = 0

    for i in d:
        if budget - i < 0:
            break

        budget -= i
        answer += 1
        
    return answer