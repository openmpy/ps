def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                s = nums[i] + nums[j] + nums[k]

                if is_prime(s) == True:
                    answer += 1
                    
    return answer