import re
import sys
s = bytes.hex(b"Hello, World!\n") 
cs = re.findall('..', s)
for c in cs:
    b = str(bin(int(c, 16)))[2:]
    b.replace("1", "l")
    b = b.replace("1", "l")
    b = b.replace("0", "1")
    b += "[I"
    sys.stdout.write(b)
