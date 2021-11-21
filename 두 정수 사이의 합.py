def solution(a, b):
    s = [a, b]
    s.sort()
    d = 0
    for i in range(s[0], s[1]+1):
        d += i
    return d

print(solution(3,5))