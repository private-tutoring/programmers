def solution(n):
    answer = []
    for i in range(n):
        if i % 2 == 0:
            answer.append("박")
        else: answer.append("수")
    return "".join(answer)