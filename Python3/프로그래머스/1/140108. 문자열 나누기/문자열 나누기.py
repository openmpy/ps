def solution(s):
    answer = 0

    start = ''
    cnt_1 = 0
    cnt_2 = 0

    for i in s:
        if cnt_1 == cnt_2:
            answer += 1
            start = i

        if i == start:
            cnt_1 += 1
        else:
            cnt_2 += 1
            
    return answer