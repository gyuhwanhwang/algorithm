def solution(board, moves):
    count = 0

    # moves 거꾸로 변환
    moves: List[int] = list(map(lambda x: x - 1, moves))
    moves.reverse()

    result = [0]
    # 바구니 쌓기
    while moves:
        current, target, pick = 0, moves.pop(), 0
        while current != len(board) and board[current][target] == 0:
            current += 1
        if current != len(board):
            pick, board[current][target] = board[current][target], pick
        if pick:
            result.append(pick)
            if result[-1] == result[-2]:
                count += 2
                result.pop(-1)
                result.pop(-1)

    return count

    # 바구니 계산
#     while result:
#         if len(result) == 1:
#             return count
#         for i in range(len(result) - 1):
#             if result[i] == result[i+1]:
#                 count += 2
#                 result[i], result[i+1] = 0, 0
#                 break
#             if i == len(result) - 2:
#                 return count
#         result = [n for n in result if n != 0]
#     return count