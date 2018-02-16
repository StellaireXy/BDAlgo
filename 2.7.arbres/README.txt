Ubuntu 16.04
Hadoop 2.7.5
Python 3.6 + HDFS3 or Java (with lots of packages)

This exercise is writen in Python (and Java)

to run the project (you have to put the input file on HDFS first)

~$ /usr/local/hadoop/bin/hdfs dfs -mkdir /test
~$ /usr/local/hadoop/bin/hdfs dfs -copyFromLocal arbres.csv /test

#Run in Python
~$ python3 YearHeightTree.py
