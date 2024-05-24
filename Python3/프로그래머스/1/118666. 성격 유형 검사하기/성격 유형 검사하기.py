def solution(survey, choices):
    ctx = {
        'R': 0,
        'C': 0,
        'J': 0,
        'A': 0
    }

    for i, n in enumerate(choices):
        if survey[i][0] == 'R':
            ctx['R'] += 4 - n
        elif survey[i][0] == 'T':
            ctx['R'] += n - 4
        elif survey[i][0] == 'C':
            ctx['C'] += 4 - n
        elif survey[i][0] == 'F':
            ctx['C'] += n - 4
        elif survey[i][0] == 'J':
            ctx['J'] += 4 - n
        elif survey[i][0] == 'M':
            ctx['J'] += n - 4
        elif survey[i][0] == 'A':
            ctx['A'] += 4 - n
        elif survey[i][0] == 'N':
            ctx['A'] += n - 4

    answer = ""

    if ctx["R"] >= 0:
        answer += "R"
    else:
        answer += "T"

    if ctx["C"] >= 0:
        answer += "C"
    else:
        answer += "F"

    if ctx["J"] >= 0:
        answer += "J"
    else:
        answer += "M"

    if ctx["A"] >= 0:
        answer += "A"
    else:
        answer += "N"
        
    return answer