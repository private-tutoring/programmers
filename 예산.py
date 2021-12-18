def solution(d, budget):
    d.sort()
    total = 0
    count = 0
    for i in range(len(d)):
        
        total += d[i]
        if not total > budget:
            count += 1
        else: return count    
            
    return count

print(solution([2, 2, 3, 3], 10))