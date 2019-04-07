#Chapter 4 projects test

spam = ['apples', 'bananas', 'tofu', 'cats']

def print_List(lst):
    strlst = ''
    for item in lst:
        if strlst == '':
            strlst = item 
        else:
            strlst += item 
    print (strlst)

a = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def tranpose_grid(grid):
        newGrid = []       
        for j in range(len(grid[0])):          #turn old grid row to column
                for i in range(len(grid)):     #turn old grid column to row
                        newGrid.append(grid[i][j])         
                print_List(newGrid)
                newGrid = []

tranpose_grid(a)

        
