def solution(n):
    arr = [True for i in range(n+1)]
    arr[0], arr[1] = False, False
    
    for i, v in enumerate(arr):
        if v == True:
            for j in range(2, len(arr)):
                if i * j >= len(arr):
                    break
                arr[i * j] = False

    return arr.count(True)
    print(arr)
    


print(solution(5))
