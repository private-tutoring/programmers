def solution(board, moves):
    stack = []
    size = len(board)
    result = 0
    for i in moves:
        i -= 1
        for j in range(size):
            if board[j][i] != 0:
                if len(stack) == 0:   
                    stack.append(board[j][i])
                elif stack[-1] == board[j][i]:
                    result += 2
                    stack.pop()
                else: stack.append(board[j][i])
                board[j][i] = 0
                break
    print(stack)
    return result

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
                