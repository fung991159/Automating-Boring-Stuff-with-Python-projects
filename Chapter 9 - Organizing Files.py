# -*- coding: cp1252 -*-

#Selective Copy
# Write a program that walks 
# through a folder tree and searches 
# for files with a certain file extension (such as .pdf or .jpg). Copy these files 
# from whatever location they are in to a new folder.


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

selectiveCopy()               