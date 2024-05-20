def solution(participant, completion):
    goal = {}

    for i in participant:
        if goal.get(i) == None:
            goal[i] = 1
        else:
            goal[i] += 1

    for i in completion:
        goal[i] -= 1

        if goal[i] == 0:
            del goal[i]

    for key in goal:
        return key