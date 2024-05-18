def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = [0] * 3

    for i in range(len(answers)):
        if answers[i] == student_1[i % 5]:
            answer[0] += 1
        if answers[i] == student_2[i % 8]:
            answer[1] += 1
        if answers[i] == student_3[i % 10]:
            answer[2] += 1

    m = max(answer)

    result = []
    for i in range(len(answer)):
        if m == answer[i]:
            result.append(i + 1)
            
    return result