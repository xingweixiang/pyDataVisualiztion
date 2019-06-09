import time
import os
import sys

# if len(sys.argv) != 2:
#     print ("Please specify filename to read")
#
# filename = sys.argv[1]
filename = 'ch02-fixed-width-1M.data'
if not os.path.isfile(filename):
    print ("Given file: \"%s\" is not a file" % filename)

with open(filename,'r') as file:
    # Move to the end of file
    filesize = os.stat(filename)[6]
    file.seek(filesize)

    # endlessly loop 
    while True:
        where = file.tell()#tell() 方法返回文件的当前位置，即文件指针当前位置。
        # try reading a line
        line = file.readline()
        # if empty, go back
        if not line:
            time.sleep(1)
            file.seek(where)
        else:
            print (line)
