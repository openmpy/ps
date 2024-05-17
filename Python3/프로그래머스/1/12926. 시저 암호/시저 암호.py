def solution(s, n):
    answer = []

    for c in s:
        new_char = ''
        if c == ' ':
            new_char += c
            answer.append(new_char)
            continue

        new_char = chr(ord(c) + n)

        if c.isupper():
            if ord(new_char) > ord('Z'):
                tmp = ord(new_char) - ord('Z')
                new_char = chr(ord('A') + tmp - 1)
        elif c.islower():
            if ord(new_char) > ord('z'):
                tmp = ord(new_char) - ord('z')
                new_char = chr(ord('a') + tmp - 1)

        answer.append(new_char)

    new_answer = ''.join(answer)
    return new_answer