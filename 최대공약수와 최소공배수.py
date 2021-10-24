
import math

def divisor(n):
    l = set()
   
    # todo: 약수 구하기
    for i in range(1, math.isqrt(n)+1):
        if n % i == 0:
            l.add(n // i)
            l.add(i)

    return l 

def solution(n, m):
    l = []

    n_div = divisor(n)
    m_div = divisor(m)

    
    for i in m_div:
        for j in n_div:
            if i == j:
                l.append(j)
    
    l.sort()
    gcm = l[-1]

    return [gcm, (n * m) // gcm]