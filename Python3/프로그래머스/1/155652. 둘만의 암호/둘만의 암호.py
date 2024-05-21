def solution(s, skip, index):
    a_to_z = []

    for i in range(26):
        a_to_z.append(chr(ord('a') + i))

    for i in skip:
        if i in a_to_z:
            a_to_z.remove(i)

    answer = ''

    for i in s:
        new_index = a_to_z.index(i) + index
        answer += a_to_z[new_index % len(a_to_z)]
        
    return answer