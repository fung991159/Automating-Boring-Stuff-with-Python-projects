import re

#Chapter 7 Practice Questions Q19-22

decimalRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
lastNameRegex = re.compile(r'^[A-Z]\w*\sNakamoto$')
sentenceRegex = re.compile(r'''(
    ^(Alice|Bob|Carol)\s
    (eats|pets|throws)\s
    (apples|cats|baseballs)
    \.$
)''',re.VERBOSE|re.IGNORECASE)

# try:
#     # test1 = decimalRegex.search('1,232')
#     # test1 = lastNameRegex.search('Satoshi Nakamoto')
#     test1 = sentenceRegex.search('Carol throws baseballs.')
#     print (test1.group())
# except:
#     print ('can\'t find')