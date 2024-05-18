def solution(array, commands):
    answer = []

    for cmd in commands:
        nums = []
        for i in range(cmd[0] - 1, cmd[1]):
            nums.append(array[i])

        answer.append(list(sorted(nums))[cmd[2] - 1])
        
    return answer