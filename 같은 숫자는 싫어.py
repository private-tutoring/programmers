def solution(arr):

    arry = [arr[0]]
    for i in range(1, len(arr)):
        if arry[-1] == arr[i]:
            arry.append(arr[i])
    return arry



print(solution([1,1,3,3,0,1,1]))