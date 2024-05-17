def solution(s):
    s2 = s.split(' ')
    answer = []

    for string in s2:
        new_string = ""
        for i, c in enumerate(string):
            if i % 2 == 0:
                new_string += c.upper()
            else:
                new_string += c.lower()

        answer.append(new_string)

    new_answer = ' '.join(answer)
    return new_answer