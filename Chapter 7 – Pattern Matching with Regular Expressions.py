import re

#Strong Password Detection
def checkPwdStrength(pwd):
    pwdRegex_8char = re.compile('.{8,}')    #at least 8 character of anything
    pwdRegex_upperCase = re.compile('[A-Z]+')   #contains upper case
    pwdRegex_lowerCase = re.compile('[a-z]+') #contains lower case
    pwdRegex_1digit = re.compile('[\d]+') #contain at least 1 digit

    test1 = pwdRegex_8char.search(pwd)
    test2 = pwdRegex_upperCase.search(pwd)
    test3 = pwdRegex_lowerCase.search(pwd)
    test4 = pwdRegex_1digit.search(pwd)

    if None not in (test1, test2, test3, test4):
        print('Valid password!')
    else:
        print ('invalid password!')

# pwd = '1234AbCD'
# checkPwdStrength(pwd)

# Regex Version of strip()
def Regex_strip(targetString, replaceText=None):
    if replaceText == '':
        print ('please enter text to match in second parameter')
    elif '\\' in replaceText:
        stripRegex = re.compile(r'\\*')
        return stripRegex.sub('', targetString)
    elif replaceText is None:
        stripRegex = re.compile(r'\s*')
        return stripRegex.sub('', targetString)
    else:
        stripRegex = re.compile('['+replaceText+']+')
        return stripRegex.sub('', targetString)
    
textTostrip = Regex_strip('1234\\15bb\\671as', '\\')
print (textTostrip)