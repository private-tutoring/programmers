def solution(n):
    answer = 0
    s = ''
    result = []
    answer = list(str(n))
    for i in range(len(answer)):
        result.append(int(answer[i]))
    result.sort()
    result.reverse()
    for i in range(len(result)):
        s += str(result[i])
    return int(s)

print(solution(118372))