def solution(board):
    max_val = max(max(board))
    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] == 1:
                board[y][x] = min(board[y-1][x-1], board[y-1][x], board[y][x-1]) + 1
                max_val = max(max_val, board[y][x])
    return max_val ** 2



def solution2(board):
    def square(row, col):
        if row + cur[0] > len(board) or col + cur[0] > len(board[0]):
            return False
        # for i in range(row, row + cur[0]):
        #     for j in range(col, col + cur[0]):
        #         print(board[i][j])
        #         if board[i][j] == 0:
        #             return False
        if sum(board[i][j] for i in range(row, row + cur[0]) for j in range(col, col +cur[0])) != cur[0] ** 2:
            return False
        cur[0] += 1
        return True

    cur = [2]
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 1:
                while square(x, y):
                    print(x, y, cur)
                    pass
    return (cur[0] - 1) ** 2

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])