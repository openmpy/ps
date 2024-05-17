import math

def solution(n, m):
    g = math.gcd(n, m)
    answer = [g, n * m / g]
    return answer