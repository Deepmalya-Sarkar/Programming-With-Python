import re
mystr=''' +91 9933512272, +91 9984643929, +44 8746372909, +44 7463898765, +91 8976489023'''
patt=re.compile(r'\b(91) \d{10}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)