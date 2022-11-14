import math
from collections import defaultdict


def valid_solution(board):
    rows = defaultdict(list)
    cols = defaultdict(list)
    subgrids = defaultdict(list)

    for x in range(len(board)):
        for y in range(len(board[x])):
            cur_val = board[x][y]

            # 0 automatically means invalid board
            if cur_val == 0:
                return False

            try:
                # Check the current row state
                check_add_value(cur_val, rows[x])

                # Check the current column state
                check_add_value(cur_val, cols[y])

                # Check the current subgrid state
                check_add_value(cur_val, subgrids[(math.floor(x/3), math.floor(y/3))])
            except:
                return False

    return True


def check_add_value(val, values):
    if val in values:
        raise Exception()

    values.append(val)
