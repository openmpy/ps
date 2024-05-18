def solution(name, yearning, photo):
    answer = []
    ctx = {}

    for i in range(len(name)):
        ctx[name[i]] = yearning[i]

    for p in photo:
        result = 0
        for i in p:
            if ctx.get(i) != None:
                result += ctx.get(i)

        answer.append(result)
        
    return answer