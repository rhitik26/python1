import re
'''
pattern = '\st[a-z]*|^t[a-z]*'
text = 'Tom,does this text match the pattern'

#matches=re.findall(pattern, text)
matches=re.findall(pattern, text,re.I)
print(matches)
'''

phn=input("enter phone number")
pattern1='^[0-9]{10}$'


if re.match(pattern1,phn):
    print("true")
else:
    print("false")

print()