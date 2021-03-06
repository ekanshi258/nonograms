import random
import argparse


def generate(n, m):
    k = random.randint(1, n * m - 1)
    r = random.choices(population=range(0, n), k=k)
    c = random.choices(population=range(0, m), k=k)
    row_marked = {}
    col_marked = {}
    for i in range(k):
        row_marked.setdefault(r[i], set()).add(c[i])
        col_marked.setdefault(c[i], set()).add(r[i])

    #sort values
    for values in row_marked.values():
        values = sorted(values)

    for values in col_marked.values():
        values = sorted(values)

    #print(row_marked)
    #print(col_marked)

    rows = []
    for i in range(n):
        l = []
        if i not in row_marked.keys():
            l.append(0)
            rows.append(l)
            continue

        prev = -1
        current = 0
        for col in row_marked[i]:
            if prev == col - 1:
                current += 1
                prev = col
            else:
                if current != 0:
                    l.append(current)
                current = 1
                prev = col

        l.append(current)
        rows.append(l)

    columns = []
    for i in range(m):
        l = []
        if i not in col_marked.keys():
            l.append(0)
            columns.append(l)
            continue

        prev = -1
        current = 0
        for row in col_marked[i]:
            if prev == row - 1:
                current += 1
                prev = row
            else:
                if current != 0:
                    l.append(current)
                current = 1
                prev = row

        l.append(current)
        columns.append(l)

    return rows, columns, row_marked, col_marked


def print_board(rows, columns, n, m):
    for i in range(n):
        for j in range(m):
            print('.', end=' ')
        print(rows[i])

    mx = 0
    for j in range(m):
        mx = max(mx, len(columns[j]))

    for i in range(mx):
        for j in range(m):
            if len(columns[j]) > i:
                print(columns[j][i], end=' ')
            else:
                print(' ', end=' ')
        print('')


def print_solution(row_marked, n, m):
    for i in range(n):
        if i in row_marked.keys():
            for j in range(m):
                if j in row_marked[i]:
                    print('x', end=' ')
                else:
                    print('.', end=' ')
        else:
            for j in range(m):
                print('.', end=' ')
        print('')


def checker(r, c, n, m):
    print(
        "Enter your output line by line. Leave a space between each character."
    )
    print("An 'x' marks a coloured spot, '.' marks an empty spot.")
    print("Do not enter the numbers at the end of the rows and columns.")

    ansgrid = []
    for i in range(n):
        e = input()
        ansrow = e.split()
        ansgrid.append(ansrow)
    # print(ansgrid)
    print('Please wait...')

    # Checking rows
    for i in range(n):
        k = 0
        j = 0
        c_dots = 0
        c_xs = 0
        while j < m and ansrow[j] == '.':
            j += 1

        while j < m and k < len(r[i]):
            # atleast one dot before a line of x's, unless it's the first x
            if k != 0 and c_dots == 0:
                return False
            c_dots = 0
            c_xs = 0
            while j < m and ansrow[j] == 'x':
                c_xs += 1
                j += 1
            if r[i][k] != c_xs:
                return False
            else:
                k += 1

            while j < m and ansrow[j] == '.':
                j += 1
                c_dots += 1

    # Now we have the grid, check columns
    for j in range(m):
        k = 0
        i = 0
        c_dots = 0
        c_xs = 0
        while i < n and ansgrid[i][j] == '.':
            i += 1

        while i < n and k < len(c[j]):
            # atleast one dot before a line of x's, unless it's the first x
            if k != 0 and c_dots == 0:
                return False
            c_dots = 0
            c_xs = 0
            while i < n and ansgrid[i][j] == 'x':
                c_xs += 1
                i += 1
            if c[j][k] != c_xs:
                return False
            else:
                k += 1

            while i < n and ansgrid[i][j] == '.':
                i += 1
                c_dots += 1

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enter row and column numbers with --rows and --cols")
    parser.add_argument('--rows',
                        type=int,
                        required=True,
                        help="Number of Rows in the nonogram")
    parser.add_argument('--cols',
                        type=int,
                        required=True,
                        help="Number of Columns in the nonogram")
    parser.add_argument('--seed', type=int)
    parser.add_argument('--inst',
                        action='store_true',
                        help="Use if game instructions are needed")
    args = parser.parse_args()

    n = args.rows
    m = args.cols

    if args.seed is not None:
        random.seed(args.seed)

    inst = """
    Instructions: 
    -------------
    Numbers on the rows and columns show how many cells should be coloured in that row/column.
    . . [1]
    . . [0]
    1 0

    Then the solution is:
    x . [1]
    . . [0]
    1 0

    When there are multiple numbers in the row/column, such as:
    . . . . . [1, 2]
    Then there should be a gap of *at least* 1 cell between the two groups of coloured cells (1 coloured cell and then 2 consecutive coloured cells), like:
    x . x x . [1, 2]    (or)    x . . x x [1, 2]    (or)    . x . x x [1, 2]

    x -> denotes that the cell is coloured
    . -> denotes that the cell is empty
    """

    if args.inst is True:
        print(inst)

    r, c, ans_r, ans_c = generate(n, m)
    #print("rows: ", r)
    #print("columns: ", c)

    print('\nHere\'s your board:')
    print_board(r, c, n, m)

    choice = input(
        '\nPress C to enter and check your solution. \nDo you want to see a solution instead? Do not enter anything if you want to wait. Choosing \'n\' will exit the game. (Y/n)'
    )
    if choice == 'n' or choice == 'N':
        print('Bye :)')
    elif choice == 'C' or choice == 'c':
        if checker(r, c, n, m):
            print('Correct answer!')
        else:
            print('Oops, that\'s not right. Possible solution:')
            print_solution(ans_r, n, m)
    else:
        print('\nPossible solution:')
        print_solution(ans_r, n, m)
