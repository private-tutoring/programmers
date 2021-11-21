def drawmap(n, graph, arr):
    for i, v in enumerate(arr):
        b = bin(v)[2:]
        if len(b) < n:
            b = "0" * (n - len(b)) + b
            arr[i] = b
        else:
            arr[i] = b
    
    for i, v in enumerate(arr):
        for j, b in enumerate(v):
            if b == '1':
                graph[i][j] = "#"

def solution(n, arr1, arr2):
    graph = [[" "] * n for _ in range(n)]
    drawmap(n, graph, arr1)
    drawmap(n, graph, arr2)
    for i in range(len(graph)):
        r = "".join(graph[i])
        graph[i] = r
    return graph

solution(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28])


