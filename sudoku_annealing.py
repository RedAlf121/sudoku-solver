import copy
from math import exp
import random
import time

from utils import print_sudoku, pretty_print

def modified(mat):
    zeroes = lambda row: list(map(lambda cell: True if cell == 0 else False, row))
    return [zeroes(cells) for cells in mat]

def generate_neighbor(mat, voids):
    
    new_mat = copy.deepcopy(mat)

    positions = [(i, j) for i in range(9) for j in range(9) if voids[i][j]]
    
    row, col = random.choice(positions)
    
    current = new_mat[row][col]
    choices = list(set(range(1, 10)) - {current})
    new_mat[row][col] = random.choice(choices)
    
    return new_mat



def cost_function(mat):
    total_cost = 0

    #rows first
    for row in mat:
        numbers = set(row)
        total_cost+=9-len(numbers)
    #columns
    for column in range(9):
        new_var = [mat[cell][column] for cell in range(9)]
        numbers = set(new_var)
        total_cost+=9-len(numbers)
            
            
    #subsquares
    for row_gap in range(0,9,3):
        for column_gap in range(0,9,3):
            numbers = set()
            for subrow in range(3):
                for subcolumn in range(3):
                    numbers.add(mat[row_gap+subrow][column_gap+subcolumn])
            total_cost+=9-len(numbers)
            numbers.clear()
    return total_cost

def init(mat):
    randomize = lambda row: list(map(lambda cell: random.randint(1,9) if cell == 0 else cell, row))
    return [randomize(cells) for cells in mat]

def solveSudoku(mat,time_step=0):
    temperature = 100
    initial = init(mat)
    score = cost_function(initial)
    i = 1
    voids = modified(mat)
    print_sudoku(initial)
    print('\n')
    if time_step != 0:
        time.sleep(time_step)
    while score != 0 and temperature > 0.1:
        neighbor = generate_neighbor(initial,voids)
        print_sudoku(neighbor)
        print('\n')
        if time_step != 0:
            time.sleep(time_step)
        neighbor_score = cost_function(neighbor)

        delta = score-neighbor_score
        print(f"delta: {delta} temperature: {temperature}")
        if delta > 0 or random.random() < exp(delta / temperature):
            initial = neighbor
            score = neighbor_score

        temperature*=0.999
        i+=1
        if i == 1000:
            initial = init(mat)
    return initial


if __name__ == "__main__":
    mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]


    solution = solveSudoku(mat,time_step=0)

    pretty_print(solution)
    
    
    
    