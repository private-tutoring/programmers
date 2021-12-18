def solution(numbers):
    l = set()
    e = 0
    for i in range(len(numbers)-1):
        e = i + 1
        while e < len(numbers):
            l.add(numbers[i]+numbers[e])
            e += 1
        
    l = list(l)
    l.sort()
    return l


print(solution([2,1,3,4,1]))
        