import random
import argparse


def generate(n, m):
    k = random.randint(1, n*m-1)
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

    print(row_marked)
    print(col_marked)

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
            if prev == col-1:
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
            if prev == row-1:
                current += 1
                prev = row
            else:
                if current != 0:
                    l.append(current)
                current = 1
                prev = row

        l.append(current)
        columns.append(l)

    return rows, columns





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter row and column numbers with --rows and --cols")
    parser.add_argument('--rows', type=int, required=True, help="Number of Rows in the nonogram")
    parser.add_argument('--cols', type=int, required=True, help="Number of Columns in the nonogram")
    parser.add_argument('--seed', type=int)
    args = parser.parse_args()

    n = args.rows
    m = args.cols

    if args.seed is not None:
        random.seed(args.seed)

    print(n)
    print(m)

    r,c = generate(n,m)
    print("rows: ", r)
    print("columns: ", c)
