import sys
#python ch02-chunk-read.py ch02-fixed-width-1M.data
filename = sys.argv[1]

with open(filename, 'rb') as hugefile:
    chunksize = 1000
    readable = ''
    while hugefile:
        start = hugefile.tell()#tell() 方法返回文件的当前位置，即文件指针当前位置。
        print ("starting at:"), start
        file_block = ''
        for _ in range(start, start + chunksize):
            #line = hugefile.next()
            line = hugefile.readline()
            #file_block = file_block + line #TypeError: can only concatenate str (not "bytes") to str
            file_block = file_block + line.decode()#bytes与字符串的相互转化
            print ('file_block'), type(file_block), file_block
        readable = readable + file_block
        stop = hugefile.tell()
        print ('readable', type(readable), readable)
        print ('reading bytes from %s to %s' % (start, stop))
        print ('read bytes total:', len(readable))
        
        #raw_input()Python3将raw_input和input进行整合成了input....去除了raw_input()函数..
        input()

