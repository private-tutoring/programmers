def solution(n):
    answer = []
    answer2 = ""
    for i in range(len(str(n))):
        answer.append(str(n)[i])
    answer.sort(reverse=True)
    for i in answer:
        answer2 += str(i)
    return int(answer2)
print(solution(118372))