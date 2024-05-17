def solution(sizes):
    mm = ms = 0
    mm2 = ms2 = 0

    for size in sizes:
        mm = max(size[0], size[1])
        ms = min(size[0], size[1])

        mm2 = max(mm2, mm)
        ms2 = max(ms2, ms)
        
    return mm2 * ms2