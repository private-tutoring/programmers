import math

def s(num):
    diviors = set()
    for i in range(1, math.isqrt(num)+1):
        if num % i == 0:
            diviors.add(i)
    print(diviors)
    return len(diviors) * 2

def s1(num):
    count = 0
    for i in range(1, math.isqrt(num)+1):
        if num % i == 0:
            count += 1
    count *= 2
    if math.sqrt(num) == float(math.isqrt(num)): 
        count -= 1
    return count


def solution(left, right):
    f = 0
    for i in range(left, right+1):
        if s1(i) % 2 != 0:
            f -= i
        else: f += i
    return f