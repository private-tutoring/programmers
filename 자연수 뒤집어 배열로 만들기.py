def solution(n):
    result = []
    answer = list(str(n))
    for i in range(1, len(answer)+1):
        result.append(int(answer[-i]))
    return result


solution(12345)