def print_sudoku(mat):
    for row in mat:
        print(" ".join(map(str, row)))


def pretty_print(mat):
    print("".join(["-" for _ in range(23)]))
    for i in range(9):
        for j in range(9):
            print(f"{mat[i][j]}",end=" ")
            if (j+1) % 3 == 0:
                print("|",end=" ")
        print("\n")
        if (i+1) % 3 == 0:
            print("".join(["-" for _ in range(23)]))