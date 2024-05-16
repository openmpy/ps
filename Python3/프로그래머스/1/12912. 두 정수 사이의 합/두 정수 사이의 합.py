def solution(a, b):
    n = min(a, b)
    m = max(a, b)
    
    answer = sum(i for i in range(n, m + 1))
    return answer