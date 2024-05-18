import datetime

def solution(a, b):
    answer = ''
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    answer = day[datetime.datetime(2016, a, b).weekday()]
    return answer