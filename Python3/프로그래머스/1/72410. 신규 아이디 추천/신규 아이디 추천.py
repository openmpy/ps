def solution(new_id):
    # 1단계
    step = ""
    for ch in new_id:
        if ch.isupper():
            step += ch.lower()
        else:
            step += ch

    # 2단계
    step_2 = ""
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            '-', '_', '.']

    for ch in step:
        if ch in chars:
            step_2 += ch

    # 3단계
    while step_2.find("..") != -1:
        step_2 = step_2.replace("..", ".")

    # 4단계
    if step_2[0] == ".":
        step_2 = step_2[1:]
    elif step_2[-1] == ".":
        step_2 = step_2[:-1]

    # 5단계
    if len(step_2) == 0:
        step_2 = "a"

    # 6단계
    if len(step_2) >= 16:
        step_2 = step_2[0:15]

    if step_2[-1] == ".":
        step_2 = step_2[:-1]

    # 7단계
    if len(step_2) <= 2:
        step_2 += step_2[-1] * (3 - len(step_2))
        
    return step_2