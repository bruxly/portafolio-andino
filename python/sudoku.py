

def find_next_empety(puzzle):
    #recorro cada fila y cada columna
    for r in range(9):
        for c in range (9):

            if puzzle [r][c]== -1:#compruebo que las casillas esten vacias 
                return r,c
           
    return None, None #si ningún espacio en el rompecabezas está vacío (-1)
     


def is_valid(puzzle, guess, row, col):
    #averigua si la suposición en la fila/columna del 
    # rompecabezas es una suposición válida devuelve 
    # verdadero si es válido, falso de lo contrario

    #empecemos a ensanchar la fila
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #ahora la columna
    #col_vals = []
    #for i in range(9):
        #col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #y luego el cuadrado
    #esto es complicado, pero queremos llegar a donde comienza el cuadrado 3x3 
    # empieza iterar sobre los 3 valores en la fila/columna

    row_start = (row // 3)*3 # 1//3=0,5 //3 = 1,...
    col_start = (col // 3)*3

    for r in range(row_start, row_start + 3):
        for c in range (col_start, col_start + 3):
            if puzzle [r][c] == guess:
                return False
    
    return True #si llegamos aquí, estos cheques pasan


    #resolver sudoku utilizando el retroceso nuestro rompecabezas es una lista en la que cada lista interna
    # es una fila en nuestro rompecabezas devolver si existe una solución muta el rompecabezas para que sea la solución
    #(si existe la solución) paso 1: elija un lugar para adivinar


    #soluciono el suduko
def solve_sudoku(puzzle):
    row,col = find_next_empety(puzzle)

    #paso 1.1: si no queda nada, entonces hemos terminado porque solo permitimos entradas válidas
    if row is None:
        return True
        
    
    #step 2: if there is a place to put a number, 
    # then make a guess between 1 and 9 
    for guess in range(1,10): #rango(1,10) is 1,2,3....9
        #  paso 3: compruebe si esto es una suposición válida
        if is_valid(puzzle,guess,row,col):
            #paso 3.1: si esto es válido, coloque esa conjetura en el rompecabezas
            puzzle[row][col] = guess

            #¡Ahora recurra usando este rompecabezas!
            #paso 4: llama recursivamente a nuestra función
            if solve_sudoku(puzzle):
                return True
            
        #paso 5: si no es válido o si nuestra conjetura no resuelve el rompecabezas, 
        # debemos retroceder e intentar con un nuevo número
        
        puzzle[row][col] =-1 #reset the guess
        #paso 6: si ninguno de los números que intentamos funciona,
        # ¡entonces este acertijo es INRESOLVIBLE!

    return False

if __name__=='__main__':
    example_board =[
        [3, 9, -1,  -1, 5,-1,  -1,-1,-1],
        [-1,-1,-1,   2,-1,-1,  -1,-1, 5],
        [-1,-1,-1,   7, 1, 9,  -1, 8,-1],
        
        [-1, 5,-1,  -1, 6, 8,  -1,-1,-1],
        [ 2,-1, 6,  -1,-1, 3,  -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1, 4],

        [ 5,-1,-1,  -1,-1,-1,  -1,-1,-1],
        [ 6, 7,-1,   1,-1, 5,  -1, 4,-1],
        [ 1,-1, 9,  -1,-1,-1,   2,-1,-1],
    ]

    print(solve_sudoku(example_board))
    print(example_board)
    
    #fuentes de informacion adicional
    #https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
    #https://youtu.be/tDxOk9TAnJ0