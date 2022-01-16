import math
from itertools import combinations

def isPrime(num):
    for i in range(2, math.isqrt(num)+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    result = 0

    for item in combinations(nums, 3):
        if isPrime(sum(item)):
            result += 1
    return result

                




print(solution([1,2,7,6,4]	))