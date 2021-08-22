def solution(d, budget):
    count = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            count += 1
        else: return count
    return count
    