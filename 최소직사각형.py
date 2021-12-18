def solution(sizes):
    l = []
    l2 = []
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            l.append(sizes[i][0])
            l2.append(sizes[i][1])
        else:
            l.append(sizes[i][1])
            l2.append(sizes[i][0])
    l.sort(reverse=True)
    l2.sort(reverse=True)
    return l[0] * l2[0]



print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))