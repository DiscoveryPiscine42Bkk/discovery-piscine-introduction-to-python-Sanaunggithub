def checkmate(board_str):
    board = board_str.strip().split("\n")
    size = len(board)
    board = [list(row.ljust(size, '.')) for row in board]  # pad rows if needed

    king_pos = None
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return False

    def is_in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    xk, yk = king_pos

    # Pawn check (assuming upward attack, like black pawns)
    for dx, dy in [(1, -1), (1, 1)]:
        xp, yp = xk + dx, yk + dy
        if is_in_bounds(xp, yp) and board[xp][yp] == 'P':
            return True

    # Bishop/Queen diagonals
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = xk + dx, yk + dy
        while is_in_bounds(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ('B', 'Q'):
                    return True
                break
            x += dx
            y += dy

    # Rook/Queen straight lines
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = xk + dx, yk + dy
        while is_in_bounds(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ('R', 'Q'):
                    return True
                break
            x += dx
            y += dy

    return False
