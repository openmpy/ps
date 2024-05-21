def solution(keymap, targets):
    ctx = {}

    for key in keymap:
        for c in key:
            if ctx.get(c) == None:
                ctx[c] = key.index(c) + 1
            else:
                ctx[c] = min(key.index(c) + 1, ctx[c])

    answer = []

    for target in targets:
        s = 0

        for t in target:
            if ctx.get(t) != None:
                s += ctx[t]
            else:
                s = -1
                break

        answer.append(s)
        
    return answer