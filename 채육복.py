def solution(n, lost, reserve):
    # answer = n - len(lost)
    # reserve.sort(reverse=True)
    # lost.sort()
    # for i in lost:
    #     if len(reserve) == 0: break
    #     if i == reserve[-1]:
    #         answer += 1
    #         reserve.pop()
    #     elif i - 1 == reserve[-1]:
    #         answer += 1
    #         reserve.pop()
    #     elif i + 1 == reserve[-1]:
    #         answer += 1
    #         reserve.pop()
    # return answer


    realSize = n - len(lost)
    lost.sort()
    reserve.sort()

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j] = -1

    for p in lost:
        for r in range(len(reserve)):
            if reserve[r] == p - 1 or reserve[r] == p + 1:
                reserve[r] = -1
                break


    return realSize + reserve.count(-1)
    