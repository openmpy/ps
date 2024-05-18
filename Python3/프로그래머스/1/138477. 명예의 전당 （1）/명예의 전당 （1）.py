def solution(k, score):
    answer = []
    result = []

    for i in range(0, len(score)):
        answer.append(score[i])
        answer = sorted(answer, reverse = True)

        if len(answer) < k:
            result.append(answer[-1])
        else:
            result.append(answer[k - 1])
            
    return result