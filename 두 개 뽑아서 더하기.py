def solution(numbers):
    answer = set()
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1, l):
            answer.add(numbers[i] + numbers[j])
    
    return sorted(list(answer))

print(solution([2,1,3,4,1]))