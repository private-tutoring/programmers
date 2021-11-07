def solution(n):
    arr = [True for _ in range(n+1)]
    for i in range(2, len(arr)):
        if arr[i] == True:
            for j in range(2, n+1):
                if i * j > n:
                    break
                arr[i * j] = False
    return arr.count(True)-2


print(solution(5))
