import re

str = "bcdfghjklmnpqrstvwxyz"
vow = "aeiou"
print(*re.findall("(?=[%s]([%s]{2,})[%s])"%(str,vow,str),input(), re.I) or [-1], sep="\n")
