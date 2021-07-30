def solution(num):
    max_count = 0
    count = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else: num = num * 3 + 1
        count += 1
        max_count += 1
        if max_count >= 500:
            return -1
    return count