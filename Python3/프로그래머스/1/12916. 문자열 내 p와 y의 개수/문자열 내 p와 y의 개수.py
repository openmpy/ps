def solution(s):
    s = s.lower()
    answer = True

    p_cnt = y_cnt = 0

    for ch in s:
        if ch == 'p':
            p_cnt += 1
        elif ch == 'y':
            y_cnt += 1

    answer = True if p_cnt == y_cnt else False
    return answer