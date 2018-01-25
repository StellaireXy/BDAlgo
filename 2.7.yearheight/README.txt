Ubuntu 16.04
Hadoop 2.7.5
Python 3.6 + HDFS3

This exercise is writen in Python.

to run the project (you have to put the input file on HDFS first)
~$ /usr/local/hadoop/bin/hdfs dfs -mkdir /test
~$ /usr/local/hadoop/bin/hdfs dfs -copyFromLocal arbres.csv /test
~$ python3 YearHeightTree.py
