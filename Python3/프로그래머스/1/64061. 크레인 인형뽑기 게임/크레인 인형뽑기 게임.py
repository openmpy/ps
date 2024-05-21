def solution(board, moves):
    stk = [0]
    answer = 0

    for i in moves:
        idx = i - 1

        for j in range(len(board)):
            if board[j][idx] != 0:
                if stk[-1] == board[j][idx]:
                    stk.pop()
                    answer += 2
                else:
                    stk.append(board[j][idx])

                board[j][idx] = 0
                break
                
    return answer