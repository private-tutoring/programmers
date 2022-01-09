def solution(array, commands):
    l = []
    for g in range(len(commands)):
        i = commands[g][0]
        j = commands[g][1]
        k = commands[g][2]
        h = array[i-1:j]
        h.sort()
        l.append(h[k-1])
    return l

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

