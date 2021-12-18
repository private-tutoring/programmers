def solution(left, right):
    d = 0
    for i in range(left, right+1):
        f = 0
        for j in range(1, i+1):
            if i % j == 0:
                f += 1
        if f % 2 == 0:
            d += i
        else: d -= i
    return d
