from datetime import datetime
def solution(a, b):
    time1 = datetime(2016, a, b)
    l = ['MON','TUE','WED','THU','FRI','SAT','SUN']

    t = time1.weekday()
    return l[t]


print(solution(5, 24))