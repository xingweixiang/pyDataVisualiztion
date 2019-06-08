import struct
import string

mask='9s14s5s'
parse = struct.Struct(mask).unpack_from#定义读取的方式
print ('formatstring {!r}, record size: {}'.format(\
                        mask, struct.calcsize(mask)))

datafile = 'ch02-fixed-width-1M.data'#指定要读取的文件

with open(datafile, 'r') as f:
    for line in f:
        line = line.encode()
        fields = parse(line)
        print ('fields: ', [field.strip() for field in fields])#按行读取并解析成单独的字段

