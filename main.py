import chess.x8_queens as chess


test_pos = [(2, 1), (1, 4), (7, 3), (6, 7), (4, 8), (8, 6), (3, 5), (5, 2)]
print(chess.check(test_pos))

# random_test = chess.random_position(4)
random_test = chess.random_position_sh(4)
for i in random_test:
    print(i)
    print(chess.chess_notation(i))
    chess.print_position(i)
    print()
