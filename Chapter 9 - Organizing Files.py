#Selective Copy
def selectiveCopy():
    import os,shutil

    absWorkingDir = os.path.abspath()  # fill in absolute path here
    targetFolder = 'testSource'
    destinationFolder = 'testDestination'

    for folderName, subfolders, filenames in os.walk(os.path.join(absWorkingDir,targetFolder)):
        for file in filenames:
            if file.endswith('.jpg'):
                a = os.path.join(absWorkingDir,folderName, file)
                b = os.path.join(absWorkingDir,destinationFolder, file)
                shutil.copy(a,b)

#Deleting Unneeded Files      
def delUneededFiles():
    import os, pathlib, send2trash
    rootFolder = r'C:\Users\Fung\Downloads'
    targetFolder = 'testSource'
    destinationFolder = 'testDestination'
 
    for folderName, subfolders, filenames in os.walk(pathlib.Path(rootFolder,targetFolder)):
        for file in filenames:
            fileSize = os.path.getsize(pathlib.Path(folderName,file)) / (1024 *1024) #change byte to MB
            if fileSize > 2:
                print (f"{file} is larger than 2MB, actual size: {round(fileSize,2)}MB")
                # send2trash.send2trash(os.path.join(folderName,file)) #delete files to recycle bin

#create test files with gaps
def createTestFile():
    import os, random
    targetFolder = r'C:\Users\Fung\Downloads\testGap'
    for i in range(100):
        f= open(os.path.join(targetFolder,f"spam_{i+1:03}.txt"),"w+")  #make sure it is 3 digit
        f.close

    #randomly delete 15 files
    usedNumber = []
    for i in range(15):
        ranNum = random.randint(1,99) #somehow deleting spam_100.txt will return file is in used error?
        ranNum = f"{ranNum:03}"
        if ranNum not in usedNumber: #make sure used number is not generate again
            usedNumber.append(ranNum)
            os.unlink(os.path.join(targetFolder,f"spam_{ranNum}.txt"))

#Filling in the Gaps
def fillInGaps():
    import os,shutil
    os.chdir(r'C:\Users\Fung\Downloads\testGap')
    targetFolder = r'C:\Users\Fung\Downloads\testGap'

    for folderName, subfolders, filenames in os.walk(targetFolder):
        i=0
        for file in filenames:
            # print (file, f"spam_{i+1:03}.txt" )
            shutil.move(file, f"spam_{i+1:03}.txt")
            i+=1

#As an added challenge, write another program that can 
#insert gaps into numbered files so that a new file can be added.
def insertGaps(insertStart, gapRange):
    import os,shutil
    os.chdir(r'C:\Users\Fung\Downloads\testGap')
    targetFolder = r'C:\Users\Fung\Downloads\testGap'
    
    for folderName, subfolders, filenames in os.walk(targetFolder):
        numberOfFiles = len(filenames)
        for file in reversed(filenames):  #loop backward
            if file != f"spam_{insertStart-1:03}.txt":                
                # print (file, f"spam_{numberOfFiles+gapRange:03}.txt" )
                shutil.move(file, f"spam_{numberOfFiles+gapRange:03}.txt" )
                numberOfFiles-=1
            else:
                break

if __name__ == "__main__":
    # selectiveCopy()    
    # delUneededFiles()
    # createTestFile()
    # fillInGaps()
    # insertGaps(51, 5)