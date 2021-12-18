def solution(left, right):
    result = 0
    for i in range(left, right+1):
        divisor = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisor += 1
        if divisor % 2 == 0:
            result += i
        else: result -= i
    return result
