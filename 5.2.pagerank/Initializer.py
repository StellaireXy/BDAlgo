#Pagerank
#Initializer
#IN:  FromNodeId \t ToNodeId
#OUT: FromNodeId 0.5 \t ToNodeId1 ToNodeId2 ...

import sys

pre_from = None

for line in sys.stdin:
    
    if line[0] != '#':
        
        curr_from, to = line.strip().split('\t', 1)
        tonode = int(to)
        
        if curr_from == pre_from:
            li += ' ' + str(tonode)
        elif pre_from == None:
            li = str(tonode)
        else:
            FromRank = pre_from + ' 0.5'
            print("%s\t%s" % (FromRank, li))
            li = str(tonode)
        
        pre_from = curr_from

FromRank = pre_from + ' 0.5'
print("%s\t%s" % (FromRank, li))

