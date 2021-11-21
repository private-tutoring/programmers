def solution(arr, divisor):
    s = []
    for i in arr:
        if i % divisor == 0:
            s.append(i)
    if len(s) == 0:
        return [-1]
    s.sort()
    return s

