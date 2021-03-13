
def initialization():
    global sudokucolumns,yes,no
    sudokucolumns=[]

    # CORRECT SUDOKU
    yes = [[2,9,5,7,4,3,8,6,1],
           [4,3,1,8,6,5,9,2,7],
           [8,7,6,1,9,2,5,4,3],
           [3,8,7,4,5,9,2,1,6],
           [6,1,2,3,8,7,4,9,5],
           [5,4,9,2,1,6,7,3,8],
           [7,6,3,5,2,4,1,8,9],
           [9,2,8,6,7,1,3,5,4],
           [1,5,4,9,3,8,6,7,2]]

    # INCORRECT SUDOKU
    no = [[1,9,5,7,4,3,8,6,2],
          [4,3,1,8,6,5,9,2,7],
          [8,7,6,1,9,2,5,4,3],
          [3,8,7,4,5,9,2,1,6],
          [6,1,2,3,8,7,4,9,5],
          [5,4,9,2,1,6,7,3,8],
          [7,3,5,2,4,1,8,9,6],
          [9,2,8,6,7,1,3,5,4],
          [2,5,4,9,3,8,6,7,1]]

def rows_validation(sudoku):
    result_row = "VALID"
    num_missing = "THIS NUMBER IS MISSING IN THE ROW"
    for row in sudoku:
        #--------------CHECKING---------------
        for number in range(1,10):
            if number not in row:
                result_row = "INVALID"
                return result_row,row,num_missing,number

    return result_row

def cubes_3x3(sudoku):
    result_3x3 = "VALID"
    num_missing = "THIS NUMBER IS MISSING IN THE 3x3 CUBES"
    cube = []
    for c in range (0,7,3):
        for j in range (0,7,3):
            for x in range(3):
                cube += (sudoku[x+j][0+c:3+c])  
            #--------------CHECKING---------------
            for number in range(1,10):
                if number not in cube:
                    result_3x3 = "INVALID"
                    return result_3x3,cube,num_missing,number
            cube = []

    return result_3x3
            
def columns_validation(sudoku):
    result_columns = "VALID"
    num_missing = "THIS NUMBER IS MISSING IN THE COLUMN"
    global sudokucolumns
    for number in range(0,9):
        for row in sudoku:
            sudokucolumns += [row[number]]
        #----------------CHECKING----------------
        for number in range(1,10):
            if number not in sudokucolumns:
                result_columns = "INVALID"
                return result_columns, sudokucolumns,num_missing,number
        sudokucolumns = []

    return result_columns

#------------------------------------------------

initialization()
print(rows_validation(yes))
print(cubes_3x3(yes))
print(columns_validation(yes))

#------------------------------------------------

        








