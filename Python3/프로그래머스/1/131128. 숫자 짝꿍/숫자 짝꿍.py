def solution(X, Y):
    arr_x = [0] * 10
    arr_y = [0] * 10
    arr_xy = [0] * 10

    for i in X:
        arr_x[ord(i) - ord('0')] += 1

    for i in Y:
        arr_y[ord(i) - ord('0')] += 1

    for i in range(10):
        arr_xy[i] = min(arr_x[i], arr_y[i])

    answer = ""

    for i in range(9, -1, -1):
        answer += str(i) * arr_xy[i]
        
    if len(answer) == 0:
        return "-1"
    
    if answer[0] == '0':
        return '0'
        
    return answer