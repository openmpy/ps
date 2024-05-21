def solution(ingredient):
    answer = 0
    burger = []

    for i in ingredient:
        burger.append(i)

        if len(burger) >= 4:
            a = burger.pop()
            b = burger.pop()
            c = burger.pop()
            d = burger.pop()

            if a == 1 and b == 3 and c == 2 and d == 1:
                answer += 1
            else:
                burger.append(d)
                burger.append(c)
                burger.append(b)
                burger.append(a)
            
    return answer