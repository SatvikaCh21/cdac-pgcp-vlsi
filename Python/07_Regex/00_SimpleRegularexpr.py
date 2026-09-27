import re #regular expression
pattern1 = r"World"  #$ -> end of the line , ^ -> beginning of the line
text ="World World"
searchnew = re.search(pattern1,text)
if searchnew:
    print("Pattern matched:",searchnew.group()) # .group() shows display of the pattern matched

import re
pattern2 = r"\d+" # \d+ -> returns one or more digits
text = "i have 2 apples and 3 oranges"
result = re.findall(pattern2,text)  #findall -> searches for all occurences, search -> one occurence
print(result)

import re
pattern3 = r"apple"
text = "I have 2 apple and 3 apples "
replaced = re.sub(pattern3,"orange",text)  #.sub() -> substitute
print(replaced)

import re
pattern4 = r"\s+" #\s+ -> one or more consecutive whitespace characters
text = "this is a test"
result = re.split(pattern4,text) #.split() -> splits into seperate strings
print(result)

import re
text = "My phone number is 123-456-7890"
result = re.sub(r"\d","*",text) #substituting digits with * to mask the number(e.g credit card,aadhar etc)
print(result)

import re
text = "Neha is Staying in US since 2000"
matches = re.findall(r'[a-zA-Z0-9]+',text)   #matches any sequence of one or more alphanumeric characters (letters and numbers)
print(matches)