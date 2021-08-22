def solution(scores):
    size = len(scores)
    real_scores = [[] for _ in range(size)]
    my_scores = []
    for i in range(size):
        for j in range(size):
            if i == j: my_scores.append(scores[i][j])
            real_scores[j].append(scores[i][j])

    for real_score in real_scores: real_score.sort()

    for i in range(size):
        if my_scores[i] == real_scores[i][0] and my_scores[i] != real_scores[i][1]:
            real_scores[i].pop(0)
        elif my_scores[i] == real_scores[i][-1] and my_scores[i] != real_scores[i][-2]:
            real_scores[i].pop()

    avg_scores = []
    answer = ''

    for i in range(size):
        avg_scores.append(sum(real_scores[i]) / len(real_scores[i]))

    for avg in avg_scores:
        if avg >= 90: answer += "A"
        elif avg >= 80: answer += "B"
        elif avg >= 70: answer += "C"
        elif avg >= 50: answer += "D"
        else: answer += "F"

    return answer
    
    



solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])