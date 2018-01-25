#Pagerank
#Mapper
#IN:  FromNodeId PageRank \t ToNodeId1 ToNodeId2 ...
#OUT: ToNodeId 1 \t (PageRank/outDegree)
#     FromNodeId 0 \t ToNodeId1 ToNodeId2 ...

import sys

for line in sys.stdin:
    
    FromRank, Tos = line.strip().split('\t', 1)
    ToList = Tos.split(' ')
    FromNodeId, PageRank = FromRank.split(' ', 1)
    pr = float(PageRank)
    
    outDegree = len(ToList)
    if outDegree != 0:
        for toId in ToList:
            toNode = toId + ' 1'
            print("%s\t%f" % (toNode, pr/outDegree))
        fromNode = FromNodeId + ' 0'
        print("%s\t%s" % (fromNode, Tos))

