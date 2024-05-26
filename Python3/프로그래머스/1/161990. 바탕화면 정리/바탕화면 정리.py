def solution(wallpaper):
    answer = [50, 50, 0, 0]

    for i, text in enumerate(wallpaper):
        if text.find("#") == -1:
            continue

        answer[0] = min(answer[0], i)
        answer[1] = min(answer[1], text.index("#"))

        answer[2] = max(answer[2], i + 1)
        answer[3] = max(answer[3], text.rindex("#") + 1)
        
    return answer