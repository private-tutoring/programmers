def solution(array, commands):
    result = []
    for d in commands:
        i, j, k = d
        answer = array[i-1:j]
        answer.sort()
        result.append(answer[k-1])
    return result
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))