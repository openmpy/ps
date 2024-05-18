def solution(k, m, score):
    score = list(sorted(score))
    answer = 0

    while len(score) >= m:
        arr = []

        for _ in range(m):
            arr.append(score.pop())

        answer += min(arr) * len(arr)
        
    return answer