import csv
import sys
filename = 'ch02-data.tab'
header = None
data = []
try:
    with open(filename) as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        header = next(reader)
        # c = 0
        # for row in reader:
        #     if c == 0:
        #         header = row
        #     else:
        #         data.append(row)
        #     c += 1
        data = [row for row in reader]
except csv.Error as e:
    print ("Error reading CSV file at line %s: %s" % (reader.line_num, e))
    sys.exit(-1)

if header:
    print (header)
    print ('===================')

for datarow in data:
    print (datarow)
