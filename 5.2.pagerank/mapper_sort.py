#PageRank
#Mapper_sort
#IN:  NodeId \t PageRank
#OUT: 500-PageRank \t NodeId

import sys

for line in sys.stdin:
    
    node, PR = line.strip().split('\t', 1)
    pagerank = 500 - float(PR)
    pr = '%.5f' %pagerank
    l = len(pr)
    pr = '0' * (9 - l) + pr
    
    print("%s\t%s" % (pr, node))

