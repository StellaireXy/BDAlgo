#PageRank
#Reducer_sort
#IN:  500-PageRank \t NodeId
#OUT: NodeId \t PageRank

import sys

for line in sys.stdin:
    
    PR, node = line.strip().split('\t', 1)
    pagerank = 500 - float(PR)
    pr = '%.5f' %pagerank
    
    print("%s\t%s" % (node, pr))

