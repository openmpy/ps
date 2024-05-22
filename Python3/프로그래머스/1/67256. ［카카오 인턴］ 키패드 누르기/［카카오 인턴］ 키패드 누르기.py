def count(pad, hand):
    if pad == 2:
        if hand == 1 or hand == 3 or hand == 5:
            return 1
        elif hand == 4 or hand == 6 or hand == 8:
            return 2
        elif hand == 0 or hand == 7 or hand == 9:
            return 3
        elif hand == 11 or hand == 13:
            return 4
    elif pad == 5:
        if hand == 2 or hand == 4 or hand == 6 or hand == 8:
            return 1
        elif hand == 0 or hand == 1 or hand == 3 or hand == 7 or hand == 9:
            return 2
        elif hand == 11 or hand == 13:
            return 3
    elif pad == 8:
        if hand == 0 or hand == 5 or hand == 7 or hand == 9:
            return 1
        elif hand == 2 or hand == 4 or hand == 6 or hand == 11 or hand == 13:
            return 2
        elif hand == 1 or hand == 3:
            return 3
    elif pad == 0:
        if hand == 8 or hand == 11 or hand == 13:
            return 1
        elif hand == 5 or hand == 7 or hand == 9:
            return 2
        elif hand == 2 or hand == 4 or hand == 6:
            return 3
        elif hand == 1 or hand == 3:
            return 4
        
    return -1

def solution(numbers, hand):
    answer = ""
    hands = [11, 13]
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            hands[0] = number
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            hands[1] = number
        else:
            if count(number, hands[0]) < count(number, hands[1]):
                answer += "L"
                hands[0] = number
            elif count(number, hands[0]) > count(number, hands[1]):
                answer += "R"
                hands[1] = number
            else:
                if hand == "left":
                    answer += "L"
                    hands[0] = number
                else:
                    answer += "R"
                    hands[1] = number
                    
    return answer