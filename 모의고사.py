def solution(answers):
    How_solve1 = [1,2,3,4,5]
    How_solve2 = [2, 1, 2, 3, 2, 4, 2, 5]
    How_solve3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_answer = [0, 1]
    two_answer = [0, 2]
    three_answer = [0, 3]
    not_yet_lucy_guys = []
    lucy_guys = []
    f = 0
    for i in range(len(answers)):
        if f >= len(How_solve1):
            f = 0
        if answers[i] == How_solve1[f]:
            one_answer[0] += 1
        f += 1
    f = 0
    for i in range(len(answers)):
        if f >= len(How_solve2):
            f = 0
        if answers[i] == How_solve2[f]:
            two_answer[0] += 1
        f += 1
    f = 0
    for i in range(len(answers)):
        if f >= len(How_solve3):
            f = 0
        if answers[i] == How_solve3[f]:
            three_answer[0] += 1
        f += 1
    not_yet_lucy_guys.append(one_answer)
    not_yet_lucy_guys.append(two_answer)
    not_yet_lucy_guys.append(three_answer)
    for i in range(3):
        not_yet_lucy_guys.sort(reverse=True)
        if not_yet_lucy_guys[0][0] == not_yet_lucy_guys[i][0]:
            lucy_guys.append(not_yet_lucy_guys[i][1])
    lucy_guys.sort()
    
    return lucy_guys



print(solution([1,2,3,4,5,2,2,2,2,2,2]))