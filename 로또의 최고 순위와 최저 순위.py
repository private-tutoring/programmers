def solution(lottos, win_nums):
    best = 0
    worst = 0
    for i in lottos:
        if i in win_nums:
            best += 1
        elif i == 0:
            best += 1
    for i in lottos:
        if i in win_nums:
            worst += 1
    if best == 6:
        best = 1
    elif best == 5:
        best = 2
    elif best == 4:
        best = 3
    elif best == 3:
        best = 4
    elif best == 2:
        best = 5
    else: best = 6

    if worst == 6:
        worst = 1
    elif worst == 5:
        worst = 2
    elif worst == 4:
        worst = 3
    elif worst == 3:
        worst = 4
    elif worst == 2:
        worst = 5
    else: worst = 6

    return [best, worst]

