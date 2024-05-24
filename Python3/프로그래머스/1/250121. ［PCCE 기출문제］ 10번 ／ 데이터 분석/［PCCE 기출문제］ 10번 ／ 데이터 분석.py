def solution(data, ext, val_ext, sort_by):
    dict = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    result = []

    for d in data:
        val = d[dict[ext]]
        if val < val_ext:
            result.append(d)

    result.sort(key = lambda x : x[dict[sort_by]])
    
    return result