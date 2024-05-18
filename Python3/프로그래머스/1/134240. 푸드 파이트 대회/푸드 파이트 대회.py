def solution(food):
    answer = ""
    
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1

        answer += str(i) * (food[i] // 2)

    reversed_answer = ''.join(list(reversed(answer)))
        
    return answer + '0' + reversed_answer