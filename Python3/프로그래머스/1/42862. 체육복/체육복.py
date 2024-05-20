def solution(n, lost, reserve):
    arr = [0] * n

    for i in lost:
        arr[i - 1] -= 1

    for i in reserve:
        arr[i - 1] += 1

    if arr[0] < 0 and arr[1] > 0:
        arr[0] += 1
        arr[1] -= 1

    if arr[n - 1] < 0 and arr[n - 2] > 0:
        arr[n - 1] += 1
        arr[n - 2] -= 1

    for i in range(1, n - 1):
        if arr[i] < 0:
            if arr[i - 1] > 0:
                arr[i] += 1
                arr[i - 1] -= 1
            elif arr[i + 1] > 0:
                arr[i] += 1
                arr[i + 1] -= 1

    answer = 0
    for i in arr:
        if i >= 0:
            answer += 1
            
    return answer