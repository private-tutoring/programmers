def solution(lottos, win_nums):
    arr_rank = [6, 6, 5, 4, 3, 2, 1]
    Z = 0
    R = 0
    for lotto in lottos:
        if lotto == 0: Z += 1
        if lotto in win_nums: R += 1
    return [arr_rank[Z+R], arr_rank[R]]
