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
            fileSize = os.path.getsize(pathlib.Path(folderName,file)) / (1024 *1024)
            if fileSize > 2:
                print (f"{file} is larger than 2MB, actual size: {round(fileSize,2)}MB")
                # send2trash.send2trash(os.path.join(folderName,file)) #delete files to recycle bin

if __name__ == "__main__":
    # selectiveCopy()    
    # delUneededFiles()