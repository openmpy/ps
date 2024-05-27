def solution(players, callings):
    ranking = {}

    for i, player in enumerate(players):
        ranking[player] = i

    for calling in callings:
        idx = ranking[calling] - 1

        tmp = players[idx]
        players[idx] = calling
        players[ranking[calling]] = tmp

        ranking[calling] -= 1
        ranking[tmp] += 1
        
    return players