def solution(a, b):
    g = 0
    for i in range(len(a)):
       g += a[i] * b[i]
    return g