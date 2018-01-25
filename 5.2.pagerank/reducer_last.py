#Pagerank
#Reducer Last
#IN:  NodeId 0 \t ToNodeId1 ToNodeId2 ...
#     NodeId 1 \t (PageRank/outDegree)
#OUT: NodeId \t PageRank

import sys

pre_node = None
beta = 0.85

for line in sys.stdin:
    
    nodebool, rest = line.strip().split('\t', 1)
    node, bo =nodebool.split(' ', 1)
    
    if node != pre_node:
        if pre_node != None:
            pagerank = 1 - beta + (beta * pagerank)
            print("%s\t%s" % (pre_node, str(pagerank)))
        pagerank = 0.0
        tolist = ''
    
    if bo == '1':
        pagerank += float(rest)
    else:
        tolist = rest
    
    pre_node = node

pagerank = 1 - beta + (beta * pagerank)
print("%s\t%s" % (pre_node, str(pagerank)))

