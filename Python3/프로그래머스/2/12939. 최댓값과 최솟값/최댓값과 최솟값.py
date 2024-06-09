def solution(s):
    arr = list(map(int, s.split()))
    arr.sort()

    answer = "{} {}".format(arr[0], arr[-1])
    return answer