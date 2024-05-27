def get_day(number):
    return 12 * 28 * int(number[0]) + 28 * int(number[1]) + int(number[2])

def solution(today, terms, privacies):
    answer = []
    ctx = {}

    for term in terms:
        check = list(term.split(' '))
        ctx[check[0]] = int(check[1])

    for i, privacie in enumerate(privacies):
        check = list(privacie.split(' '))
        new_day = list(check[0].split('.'))

        if get_day(new_day) + 28 * ctx[check[1]] <= get_day(list(today.split('.'))):
            answer.append(i + 1)
            
    return answer