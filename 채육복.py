# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#     for i in reserve[:]:
#         if i in lost:
#             reserve.remove(i)
#             lost.remove(i)
#     for i in lost[:]:
#         for j in reserve[:]:
#             if i-1 == j or i+1 == j:
#                 reserve.remove(j)
#                 lost.remove(i)
#                 break
#     return n - len(lost)


# print(solution(2, [2, 1], [1, 2]))



def solution(n, lost, reserve):
    # lost에도 있고 reserve에도 있을때
    for i in reserve[:]:
        if i in lost[:]:
            reserve.remove(i)
            lost.remove(i)
    for i in lost[:]:
        for j in reserve[:]:
            if i == j-1 or i == j+1:
                lost.remove(i)
                reserve.remove(j)
    return n - len(lost)

solution(5, [4,2,1], [3,5,1])