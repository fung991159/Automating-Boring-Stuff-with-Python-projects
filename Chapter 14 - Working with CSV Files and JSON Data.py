import os, csv, openpyxl

#Excel-to-CSV Converter
def excel_to_CSV(path):
    os.chdir(path)
    for excelFile in os.listdir('.'):
        if excelFile.split('.')[1] != 'xlsx': # Skip non-xlsx files, load the workbook object.
            pass
        else:
            wb = openpyxl.load_workbook(excelFile)
            for sheetName in wb.get_sheet_names():
                # Loop through every sheet in the workbook.
                sheet = wb[sheetName]
                
                # Create the CSV filename from the Excel filename and sheet title.
                csvFileName = excelFile.split('.')[0] +'_'+ sheetName + '.csv'

                # Create the csv.writer object for this CSV file.
                with open(csvFileName, 'w', newline='') as csvFile: 
                    outputWriter = csv.writer(csvFile)
                    # Loop through every row in the sheet.
                    for rowNum in range(1, sheet.max_row + 1):
                        rowData = []    # append each cell to this list
                        # Loop through each cell in the row.
                        for colNum in range(1, sheet.max_column + 1):
                            # Append each cell's data to rowData.
                            rowData.append(sheet.cell(rowNum, colNum).value)
                            
                            # Write the rowData list to the CSV file.
                        outputWriter.writerow(rowData)
                    
if __name__ == "__main__":
    path = os.path.join(r'C:\\', r'\Users\Fung\Downloads\testCSV')
    excel_to_CSV(path)
