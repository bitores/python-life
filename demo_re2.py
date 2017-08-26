import re

pattern = re.compile(r'hello')
match = pattern.match('hello world!')
if match:
    print match.group()
    
p=re.match(r'hello','hello world!')
print p.group()



# a <==> b
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

