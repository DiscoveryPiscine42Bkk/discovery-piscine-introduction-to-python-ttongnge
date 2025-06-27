import itertools
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def relocate_to_checkmate(board_string):
    board_lines = board_string.strip().split('\n')
    size = len(board_lines)
    board = [list(row) for row in board_lines]

    pieces = []
    king_pos = None

    for i in range(size):
        for j in range(size):
            cell = board[i][j]
            if cell == 'K':
                king_pos = (i, j)
            elif cell in ['R', 'B', 'Q', 'P']:
                pieces.append((cell, (i, j)))

    if not king_pos:
        print("Error: No king found.")
        return

    empty_positions = [(i, j) for i in range(size) for j in range(size)
                       if board[i][j] == '.' or board[i][j] == 'K']
    empty_positions = [pos for pos in empty_positions if pos != king_pos]

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    def is_attacked(x, y, brd):
        pawn_dirs = [(-1, -1), (-1, 1)]
        bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queen_dirs = bishop_dirs + rook_dirs

        for dx, dy in pawn_dirs:
            px, py = x + dx, y + dy
            if in_bounds(px, py) and brd[px][py] == 'P':
                return True

        for dx, dy in bishop_dirs:
            px, py = x + dx, y + dy
            while in_bounds(px, py):
                p = brd[px][py]
                if p in ['B', 'Q']:
                    return True
                elif p != '.':
                    break
                px += dx
                py += dy

        for dx, dy in rook_dirs:
            px, py = x + dx, y + dy
            while in_bounds(px, py):
                p = brd[px][py]
                if p in ['R', 'Q']:
                    return True
                elif p != '.':
                    break
                px += dx
                py += dy

        return False

    def is_checkmate(brd, kx, ky):
        king_dirs = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),          (0, 1),
                     (1, -1), (1, 0), (1, 1)]
        if not is_attacked(kx, ky, brd):
            return False
        for dx, dy in king_dirs:
            nx, ny = kx + dx, ky + dy
            if in_bounds(nx, ny) and brd[nx][ny] == '.':
                if not is_attacked(nx, ny, brd):
                    return False
        return True

    def score_board(brd, new_positions):
        piece_priority = {'Q': 1, 'R': 2, 'B': 3, 'P': 4}  # lower is better
        used_pieces = len(new_positions)
        total_distance = sum(abs(x1 - x2) + abs(y1 - y2) for (_, (x1, y1)), (x2, y2) in new_positions)
        unique_threats = sum(is_attacked(kx + dx, ky + dy, brd) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0))
        priority_score = sum(piece_priority[piece] for piece, _ in [p for p, _ in new_positions])
        return (used_pieces, total_distance, -unique_threats, priority_score)

    def draw_chessboard(board_matrix, title="Board"):
        fig, ax = plt.subplots()
        ax.set_xlim(0, size)
        ax.set_ylim(0, size)
        ax.set_aspect('equal')
        ax.set_xticks(range(size))
        ax.set_yticks(range(size))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_title(title)

        for x in range(size):
            for y in range(size):
                color = 'white' if (x + y) % 2 == 0 else 'gray'
                rect = patches.Rectangle((y, size - x - 1), 1, 1, facecolor=color)
                ax.add_patch(rect)

        for i in range(size):
            for j in range(size):
                cell = board_matrix[i][j]
                if cell != '.':
                    ax.text(j + 0.5, size - i - 1 + 0.5, cell, ha='center', va='center', fontsize=16, fontweight='bold')

        plt.grid(True)
        plt.show()

    kx, ky = king_pos
    best_board = None
    best_score = None
    best_moves = []

    for positions in itertools.permutations(empty_positions, len(pieces)):
        new_board = [['.' for _ in range(size)] for _ in range(size)]
        new_board[kx][ky] = 'K'
        new_positions = []
        valid = True

        for (piece, (ox, oy)), (nx, ny) in zip(pieces, positions):
            if new_board[nx][ny] != '.':
                valid = False
                break
            new_board[nx][ny] = piece
            new_positions.append(((piece, (ox, oy)), (nx, ny)))

        if not valid:
            continue

        if is_checkmate(new_board, kx, ky):
            score = score_board(new_board, new_positions)
            if best_score is None or score < best_score:
                best_score = score
                best_board = new_board
                best_moves = new_positions

    if best_board:
        print("Best checkmate configuration:")
        for row in best_board:
            print(''.join(row))

        print("\nPiece movement summary:")
        print("{:<6} {:<10} {:<10} {:<10}".format("Piece", "From", "To", "Distance"))
        print("-" * 40)
        for (piece, (ox, oy)), (nx, ny) in best_moves:
            distance = abs(ox - nx) + abs(oy - ny)
            print("{:<6} ({},{})     ({},{})     {:<10}".format(piece, ox, oy, nx, ny, distance))

        print("\nExplanation:")
        print("- Each row above shows the piece, its original and final position, and how many squares it moved.")
        print("- This solution was chosen based on fewest pieces moved, minimal distance, maximum threat coverage, and piece effectiveness.")

        draw_chessboard(board, "Initial Board")
        draw_chessboard(best_board, "Best Checkmate Configuration")
    else:
        print("No checkmate configuration found.")