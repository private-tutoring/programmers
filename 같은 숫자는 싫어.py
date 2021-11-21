def solution(arr):
    lis = [arr[0]]
    for i in arr:
        if lis[-1] != i:
            lis.append(i)
    return lis

print(solution([4, 4, 4, 3, 3]))