def checkmate(board_str):
    # Convert each row string into a list of characters(2D Grid)
    board = board_str.strip().split("\n")
    size = len(board)

    board = [list(row) for row in board]

    # find king position
    # Once found, stores its position as (x, y) (row, col)
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    # If no King is found, exit early
    if not king_pos:
        return

    # Prevents checking positions outside the board
    def is_in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    xk, yk = king_pos

    # Pawns attack diagonally down-left and down-right ((1,-1) and (1,1))
    # If a pawn is in either of those positions → King is in check
    for dx, dy in [(1, -1), (1, 1)]:
        xp, yp = xk + dx, yk + dy
        if is_in_bounds(xp, yp) and board[xp][yp] == 'P':
            print("Success")
            return

    # If a Bishop or Queen is found in a clear diagonal line → check diagonals outward
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = xk + dx, yk + dy
        while is_in_bounds(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # If a Rook or Queen has line of sight → check  up/down/left/right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = xk + dx, yk + dy
        while is_in_bounds(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # If not in "check"
    print("Fail")