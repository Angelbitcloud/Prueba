import re 

print (re.sub("(\d+)\+(\d+)",
             lambda m: str(int(m.group(1))+int(m.group(2))),
             "2 + 10 / 2 - 20"))

a = "Hello world" 
b = "2 + 10 / 2 - 20" 
c = "(2 + 10) / 2 - 20" 
d = "(2 + 10 / 2 - 20"

