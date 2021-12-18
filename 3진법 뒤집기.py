def solution(n):
    d = ""
    a = 0
    while n > 2:
        d += str(n % 3)
        n = n // 3
    d += str(n)
    return int(d,3)
    
