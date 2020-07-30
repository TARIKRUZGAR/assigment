sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

def sudoku_convert(sudoku):
    
    for i in range(9):
        new=""
        if i == 0 or i == 3 or i == 6:
            print("- - - - - - - - - - - - - - -")
        for j in range(9):
            new+=(str(sudoku[i][j])+'  ')
            if j==2 or j==5:
                new+=("| ")
        print(new)       
        



    print("- - - - - - - - - - - - - - -")
            
sudoku_convert(sudoku)