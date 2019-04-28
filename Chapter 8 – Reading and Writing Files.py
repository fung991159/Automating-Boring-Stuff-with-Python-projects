# Mad Libs
# Create a Mad Libs program that reads in text files 
# and lets the user add their own text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

def madLibs(): 
    import re,os 
    sourceFolder = r'C:\Users\Fung\Documents\vsc git repository\Automating-Boring-Stuff-with-Python-projects'

    with open(os.path.join(sourceFolder,'old_text.txt'),'r') as txt:
        txtList = txt.readlines()

    newlineList=[] 
    numberofLine=len(txtList) #for omitting adding newline to last line
    currentLine = 1
    generalRegex = re.compile(r'adjective|noun|verb', re.IGNORECASE)
    
    for line in txtList:
        eachLine = line.split()  #split each line in group
        endOfList = len(eachLine)  #for addingback the newline
        for word in eachLine:
            mo = generalRegex.search(word)
            if mo is not None:    #key words found
                if mo.group().lower() == 'adjective':
                    print('Enter an adjective:')
                else:
                    print(f'Enter a {mo.group().lower()}:')
                userInput = input()
                newlineList.append(userInput)
            else:
                newlineList.append(word)
        if currentLine < numberofLine:  #add new line for each line except last line
            currentLine += 1
            # add newline to the last item in list to avoid extra space
            newlineList[len(newlineList)-1] = newlineList[len(newlineList)-1] + "\n"
        #write replaced string line into a new txt file
        with open(os.path.join(sourceFolder,'new_text.txt'),'w') as newTxt:
            print(newlineList)
            newTxt.write(' '.join(newlineList))

# Regex Search
# Write a program that opens all .txt files in a folder and searches 
# for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

def regexSearch():
    import os, re
    print(r'Please input regular expression you want to search for:')
    regexString = input()
    searchRegex = re.compile(regexString)
    targetFolder = r'C:\Users\Fung\Downloads\testGap'
    keyWordFlag = False
    
    for folderName,subFolder,filenames in os.walk(targetFolder):
        for file in filenames:
            with open (os.path.join(folderName,file)) as f:
                lineList = f.readlines()
                for line in lineList:
                    if searchRegex.search(line) is not None:
                        keyWordFlag = True
                        print (f'Keyword has been found in {os.path.join(folderName,file)}!')

    if keyWordFlag == False:
        print(f'There are no text matches "{regexString}!')

if __name__ == "__main__":
    # madLibs()
    # regexSearch()