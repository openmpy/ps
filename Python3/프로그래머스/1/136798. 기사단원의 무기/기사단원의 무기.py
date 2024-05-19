def divisor_count(n):
    arr = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            arr.append(n // i)
            arr.append(i)

    return len(set(arr))

def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        if divisor_count(i) > limit:
            answer += power
        else:
            answer += divisor_count(i)
            
    return answer