def solution(numbers):
    d = 0
    s = 1
    for _ in range(9):
        if s in numbers:
            s += 1
        else: 
            d += s
            s += 1
    return d


print(solution([5,8,4]))