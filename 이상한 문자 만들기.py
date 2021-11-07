def solution(s):
    p = ''
    answer = []
    s = s.split(' ')
    for o in s:
        for i in range(len(o)):
            if i % 2 == 0:
                p += o[i].upper()
            else: p += o[i].lower()
        answer.append(p)
        p = ''
    return " ".join(answer)


print(solution("try hello world"))