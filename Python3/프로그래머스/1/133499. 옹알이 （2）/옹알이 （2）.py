def solution(babbling):
    call = ["aya", "ye", "woo", "ma"]
    no_call = ["ayaaya", "yeye", "woowoo", "mama"]

    answer = 0

    for text in babbling:
        for no in no_call:
            text = text.replace(no, '#')
        for yes in call:
            text = text.replace(yes, '.')

        if text.count('.') == len(text):
            answer += 1
            
    return answer