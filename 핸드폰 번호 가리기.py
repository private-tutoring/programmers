def solution(p):
    p = list(p)
    for i in range(len(p)-4):
        p[i] = '*'
    return "".join(p)

print(solution("01091382342"))