import re

txt = "The quick brown fox"
x = re.search("quick", txt)
print(x)

txt = "User ID: 505"
x = re.findall("\d", txt)
print(x)

txt = "Python is amazing"
x = re.split("\s", txt)
print(x)

txt = "I love apple"
x = re.sub("apple", "orange", txt)
print(x)

txt = "Error at line 10"
x = re.findall("[a-z]", txt)
print(x)
