from random import randint, sample


_abc = "abcdefgh"


def check(coordinates_list):
    coordinates_list = list(set(coordinates_list))
    flag = True
    try:
        letters = [int(x[0]) for x in coordinates_list]
        nums = [int(x[1]) for x in coordinates_list]
        l = len(coordinates_list)
        if not all(1 <= x <= 8 for x in letters) or not all((1 <= x <= 8 for x in nums)):
            raise Exception('Неверная позиция')
    except IndexError:
        pass
    for i in range(0, l-1):
        for j in range(i+1, l):
            if letters[i] == letters[j] or nums[i] == nums[j] \
                    or abs(letters[i] - letters[j]) == abs(nums[i] - nums[j]):
                return False
    return True

# прям печально долго ищет, как обезьяны печатающие войну и мир.
# по идее работает, но на практике терпения не хватило дождаться
def random_position(user_num):
    positions = []
    count = 0
    while count < user_num:
        position = set()
        i = 0
        while i < 8:
            print(i)
            x = randint(1, 8)
            y = randint(1, 8)
            if (x, y) not in position:
                position.add((x, y))
                i += 1
        if check(position):
            for i in positions:
                if position == i:
                    break
            positions.append(position)
            count += 1
    print(positions)


# чуть менее рандомно, но зато гораздо быстрее и всё ещё типа случайно
def random_position_sh(user_num):
    shuf = [1, 2, 3, 4, 5, 6, 7, 8]
    positions = []
    count = 0
    while count < user_num:
        flag = True
        position = set()
        x_list = sample(shuf, 8)
        y_list = sample(shuf, 8)
        for i in range(8):
            position.add((x_list[i], y_list[i]))
        if check(position):
            for i in positions:
                if set(position) == set(i):
                    flag = False
                    break
            if flag:
                positions.append(position)
                count += 1
    return positions


# кривенько, но для наглядности результата добавил
def print_position(user_list):
    chess_board = [[None for i in range(9)] for j in range(9)]
    for i in range(0,8):
        chess_board[i][0] = 8-i
    chess_board[8][0] = "  "
    for i in range(1, 9):
        if i == 1:
            chess_board[8][i] = _abc[i - 1]
        elif i == 5:
            chess_board[8][i] = "  " + _abc[i - 1]
        else:
            chess_board[8][i] = " " + _abc[i - 1]
    for i in range(0,8):
        for j in range(1,9):
            if (i+j)%2 == 0:
                chess_board[i][j] = "⬛"
            else:
                chess_board[i][j] = "⬜"
    for i in user_list:
        chess_board[8-i[1]][i[0]] = "♛"
    for i in chess_board:
        print(*i)


def chess_notation(user_list):
    res = [_abc[x[0]-1]+str(x[1]) for x in user_list]
    return res
