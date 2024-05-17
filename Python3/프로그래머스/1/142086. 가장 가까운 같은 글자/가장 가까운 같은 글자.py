def solution(s):
    check = [-1] * 26
    answer = []

    for i, ch in enumerate(s):
        idx = ord(ch) - ord('a')

        if check[idx] == -1:
            answer.append(-1)
        else:
            answer.append(i - check[idx])

        check[idx] = i
        
    return answer