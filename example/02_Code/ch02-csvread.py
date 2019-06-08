#!/usr/bin/env python
import csv
import sys
filename = 'ch02-data.csv'
data = []
header = None
try:
    with open(filename) as f:#打开文件
        reader = csv.reader(f)#读取
        header = next(reader)
        # c = 0
        # for row in reader:
        #     if c == 0:
        #         header = row#读取头行
        #     else:
        #         data.append(row)#读取剩余行
        #     c += 1
        data = [row for row in reader]
except csv.Error as e:
    print ("Error reading CSV file at line %s: %s") % (reader.line_num, e)
    sys.exit(-1)
if header:
    print (header)
    print ('==================')
for datarow in data:
    print (datarow)
