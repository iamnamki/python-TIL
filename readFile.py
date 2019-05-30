import sys , os

import mysys
mysys.clear()

print("file : ", __file__)
print("dirname : ", os.path.dirname(__file__))
print("abspath : " , os.path.abspath(__file__))


print(sys.argv, len (sys.argv))

def print_sys_vars() :
    for i in [sys.version, sys.copyright, sys.platform] :
        print(" --> ", i)

sa = sys.argv #파라메터값 밭아오기 $>python test.py aa bb ---> [test.py , aa , bb]
if len(sa) < 2:
    sys.exit()

with open(sa[1], "r", encoding="utf-8") as file:
    for line in file :
        print(line.strip())