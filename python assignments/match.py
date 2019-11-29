
import re

pattern = '\st[a-z]*'
text="does this text match the pattern?"


matches=re.finditer(pattern, text)
for match in matches:


    print( match.start(),match.end(),text[match.start():match.end()])


pattern1 = '\st[a-z]*|^t[a-z]*'
text1="tom,does this text match the pattern?"

#Find iter
matches=re.finditer(pattern1, text1)
for match in matches:


    print( match.start(),match.end(),text[match.start():match.end()])
