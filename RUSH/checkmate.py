complete rush
def checkmate(board_string):
    file = board_string.strip().split('\n')
    rank = len(file)

    #square board only, ensures valid board
    if any(len(line) != rank for line in file):
        print("Error")
        return

    board = [list(line) for line in file]
    size = rank

    #Find King's position
    king = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king = (i, j)
                break
        if king:
            break

    if not king:
        print("Error")
        return

    kx, ky = king

    #determine direction of Pawn Bishop Rook Queen and King
    pawn_dirs = [(-1, -1), (-1, 1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dirs = bishop_dirs + rook_dirs
    king_dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    #attack types
    def is_attacked(x, y):
        #Check Pawn
        for dx, dy in pawn_dirs:
            px, py = x + dx, y + dy
            if in_bounds(px, py) and board[px][py] == 'P':
                return True

        #Check Bishop or Queen (diagonal)
        for dx, dy in bishop_dirs:
            px, py = x + dx, y + dy
            while in_bounds(px, py):
                piece = board[px][py]
                if piece == 'B' or piece == 'Q':
                    return True
                elif piece != '.':
                    break
                px += dx
                py += dy

        #Check Rook or Queen (straight)
        for dx, dy in rook_dirs:
            px, py = x + dx, y + dy
            while in_bounds(px, py):
                piece = board[px][py]
                if piece == 'R' or piece == 'Q':
                    return True
                elif piece != '.':
                    break
                px += dx
                py += dy

        return False

    #King in check?

    in_check = is_attacked(kx, ky)

    if not in_check:
        print("Fail")
        return

    for dx, dy in king_dirs:
        nx, ny = kx + dx, ky + dy
        if in_bounds(nx, ny) and board[nx][ny] == '.':
            if not is_attacked(nx, ny):
                print("Success")  #In check, but not checkmate
                return

    print("Check mate success")  #No escape moves = checkmate
    