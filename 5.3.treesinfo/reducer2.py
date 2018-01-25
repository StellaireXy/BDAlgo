#Compute the height of the highest tree of each type
#Reducer
#OUT: type \t heightest

import sys

pre_type = None

for line in sys.stdin:
    
    type_height, nothing = line.strip().split('\t', 1)
    type, height = type_height.split(' ', 1)
    
    if type != pre_type and pre_type != None:
        print("%s\t%.2f" % (pre_type, pre_height))
    
    pre_type = type
    pre_height = float(height)
    
print("%s\t%s" % (pre_type, pre_height))
