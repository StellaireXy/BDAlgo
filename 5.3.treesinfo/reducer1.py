#Compute the number of trees by type
#Reducer1
#OUT: type \t count

import sys

pre_type = None
total = 0

for line in sys.stdin:
    
    curr_type, count = line.strip().split('\t', 1)
    if pre_type == None:
        pre_type = curr_type
    if curr_type != pre_type:
        print("%s\t%s" % (pre_type, str(total)))
        total = 0
    
    pre_type = curr_type
    total += 1

print("%s\t%s" % (pre_type, str(total)))
