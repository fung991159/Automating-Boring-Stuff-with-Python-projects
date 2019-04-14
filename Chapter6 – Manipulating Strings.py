tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)

    #find longest string in each list
    k = 0
    for element in range(len(table)):
        colWidths[k] = len(max(table[k], key = len))
        k+=1

    j = 0 
    for element in range(len(table[0])):   
        newList = []
        i = 0
        for subList in range(len(table)):  
            #append to new list
            newList.append(tableData[i][j].rjust(colWidths[i]))
            i += 1
        newString = ' '.join(newList)
        print(newString.rjust(colWidths[0]))
        j += 1

printTable(tableData)
