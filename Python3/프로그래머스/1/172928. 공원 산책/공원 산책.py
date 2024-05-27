def solution(park, routes):
    world = [0, 0]

    for i, text in enumerate(park):
        if 'S' in text:
            world[0], world[1] = i, text.index('S')

    for route in routes:
        text = route.split(' ')
        before = [world[0], world[1]]

        # 동
        if text[0] == 'E':
            for i in range(int(text[1])):
                world[1] += 1

                if world[1] == len(park[0]):
                    world[0], world[1] = before[0], before[1]
                    break
                if park[world[0]][world[1]] == 'X':
                    world[0], world[1] = before[0], before[1]
                    break

        # 서
        if text[0] == 'W':
            for i in range(int(text[1])):
                world[1] -= 1

                if world[1] == -1:
                    world[0], world[1] = before[0], before[1]
                    break
                if park[world[0]][world[1]] == 'X':
                    world[0], world[1] = before[0], before[1]
                    break

        # 남
        if text[0] == 'S':
            for i in range(int(text[1])):
                world[0] += 1

                if world[0] == len(park):
                    world[0], world[1] = before[0], before[1]
                    break
                if park[world[0]][world[1]] == 'X':
                    world[0], world[1] = before[0], before[1]
                    break

        # 북
        if text[0] == 'N':
            for i in range(int(text[1])):
                world[0] -= 1

                if world[0] == -1:
                    world[0], world[1] = before[0], before[1]
                    break
                if park[world[0]][world[1]] == 'X':
                    world[0], world[1] = before[0], before[1]
                    break
                    
    return world