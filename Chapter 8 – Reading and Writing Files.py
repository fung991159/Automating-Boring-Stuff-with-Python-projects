# Mad Libs
# Create a Mad Libs program that reads in text files 
# and lets the user add their own text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
import fnmatch
import string
import re

helloFile = open(r'C:\Users\Fung\Documents\vsc git repository\Automating-Boring-Stuff-with-Python-projects\text.txt')
a = helloFile.readlines()

#:read text file for keyword
with open(r'C:\Users\Fung\Documents\vsc git repository\Automating-Boring-Stuff-with-Python-projects\text.txt') as f:
    content = " ".join(line.strip() for line in f)
    wordList = content.split()
    
keyWordList = ['ADJECTIVE', 'NOUN', 'VERB']
cleanWordList =[]
keyWordPos = []
keyWordStr = []
punRegex = re.compile(r'\W') #remove punctuation 
for word in wordList:
    cleanWordList.append(punRegex.sub('',word))
i=0 
for word in cleanWordList:
    if word in keyWordList:
        keyWordPos.append(i)
        keyWordStr.append(word)
    i+=1

# create a input textfile with appropriate heading
replaceStr=[]
for i in range(len(keyWordStr)):
    if keyWordStr[i] == 'ADJECTIVE':
        print('Enter an adjective:')
    else:
        print('Enter a {}:'.format(keyWordStr[i].lower()))
    replaceStr.append(input())

#The results should be printed to the screen and saved to a new text file.
newWordList = []

for i in range(len(keyWordStr)):
    wordList = wordList[keyWordPos[i]]
print (wordList)
