Ubuntu 16.04
Hadoop 2.7.5
Python 3.6

to run the project
~$ bash pagerank.sh

Steps:
1. Initializer
#IN:  FromNodeId \t ToNodeId
#OUT: FromNodeId 0.5 \t ToNodeId1 ToNodeId2 ...

2. Iteration (Mapper - Reducer) 
Mapper
#OUT: ToNodeId 1 \t (PageRank/outDegree)
#     FromNodeId 0 \t ToNodeId1 ToNodeId2 ...
Reducer
#OUT: NodeId PageRank \t ToNodeId1 ToNodeId2 ...

3. Mapper - Reducer_last
Mapper
#OUT: ToNodeId 1 \t (PageRank/outDegree)
#     FromNodeId 0 \t ToNodeId1 ToNodeId2 ...
Reducer_last
#OUT: NodeId \t PageRank

4. Mapper_sort - Rreducer_sort
Mapper_sort
#OUT: PageRank \t NodeId
Reducer_sort
#OUT: NodeId \t PageRank
