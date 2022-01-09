def solution(answers):
    count1 = [0, 1]
    count2 = [0, 2]
    count3 = [0, 3]
    lucky = []
    lcky2 = []
    su_po_ja_1 = [1, 2, 3, 4, 5]
    su_po_ja_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su_po_ja_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    d = 0
    for i in range(len(answers)):
        if d >= len(su_po_ja_1):
            d = 0
        if answers[i] == su_po_ja_1[d]:
            count1[0] += 1
        d += 1
    d = 0
    for i in range(len(answers)):
        if d >= len(su_po_ja_2):
            d = 0
        if answers[i] == su_po_ja_2[d]:
            count2[0] += 1
        d += 1
    d = 0
    for i in range(len(answers)):
        if d >= len(su_po_ja_3):
            d = 0
        if answers[i] == su_po_ja_3[d]:
            count3[0] += 1
        d += 1
    lucky.append(count1)
    lucky.append(count2)
    lucky.append(count3)
    for i in range(3):
        lucky.sort(reverse=True)
        if lucky[0][0] == lucky[i][0]:
            lcky2.append(lucky[i][1])
    lcky2.sort()
    return lcky2


print(solution([1,3,2,5,3,4,1,3,2,4,5,2]))
    
