Ubuntu 16.04
Hadoop 2.7.5
Python 3.6

to run the project:
~$ bash treesinfo.sh

Write some MapReduce programs that :

1. Compute the number of trees by type
Mapper OUT: type \t 1
Reducer OUT: type \t sum

2. Compute the height of the highest tree of each type
Mapper OUT: type height \t ...
Reducer OUT: type \t heightest

3. Computer the borough (arrondi) of the oldest tree in Paris
Mapper OUT: old \t borough
Reducer OUT: oldest \t borough
