import sys , os

import clearCmd
clearCmd.clear()

# print("file : ", __file__)
# print("dirname : ", os.path.dirname(__file__))
# print("abspath : " , os.path.abspath(__file__))

dir_name = os.path.dirname(__file__) 
print(" dir_name : ", dir_name)         #dir_name :
abs_path = os.path.abspath(dir_name)
print( " abs_ path : " , abs_path)      #abs_ path :  D:\python_TIL
up_dir = os.path.join(abs_path, '..')
print("up_dir : ", up_dir)              #up_dir :  D:\python_TIL\..
path = os.path.abspath(up_dir)
print("path : ", path)                  #path :  D:\


print(sys.argv, len (sys.argv)) # >>> (python) D:\python_TIL>python readFile.py ipdbTest.py
                                # ['readFile.py', 'ipdbTest.py'] 2

def print_sys_vars() :
    for i in [sys.version, sys.copyright, sys.platform] :
        print(" --> ", i)

sysargv = sys.argv  # argument 받아오기 
                    # >>> python test.py aa bb 
                    # [test.py , aa , bb]
                    
if len(sysargv) < 2:
    sys.exit()

with open(sysargv[1], "r", encoding="utf-8") as file: #sysargv에 파일을 오픈 -> 읽기 -> 자동 close
    for line in file :
        print(line.strip())