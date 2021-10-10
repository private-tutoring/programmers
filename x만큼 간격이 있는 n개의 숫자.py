def solution(x, n):
    s = x
    answer = [x]
    for i in range(n-1):
        x += s
        answer.append(x)
    return answer