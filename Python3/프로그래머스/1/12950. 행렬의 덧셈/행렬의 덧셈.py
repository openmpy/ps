def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        l = []

        for x, y in zip(i, j):
            l.append(x + y)

        answer.append(l)
        
    return answer