def solution(lottos, win_nums):
    answer = 0
    same_count = 0

    rank = {
      1: 6,
      2: 5,
      3: 4,
      4: 3,
      5: 2,
      6: 1
    }

    for i in lottos:
        if i == 0:
            continue

        for j in win_nums:
            if i == j:
                same_count += 1

    up_rank = same_count + lottos.count(0)
    if up_rank < 2:
        up_rank = 1

    down_rank = same_count
    if down_rank < 2:
        down_rank = 1

    answer = (rank[up_rank], rank[down_rank])
    
    return answer