def solution(absolutes, signs):
    answer = 0

    for i, check in enumerate(signs):
        if check == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
            
    return answer