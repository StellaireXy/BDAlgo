#!/bin/bash
#this shell is to run 5.3. MapReduce

echo "Copy the input file from local ..."
/usr/local/hadoop/bin/hadoop fs -rm -r /test
/usr/local/hadoop/bin/hadoop fs -mkdir /test
/usr/local/hadoop/bin/hadoop fs -mkdir /test/input
/usr/local/hadoop/bin/hadoop fs -copyFromLocal /home/hadoop/Documents/5.3.treesinfo/input/arbres.csv /test/input

echo "1st MapReduce: compute the number of trees by type ..."
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.3.treesinfo/mapper1.py" -mapper "python3 /home/hadoop/Documents/5.3.treesinfo/mapper1.py" \
-file "/home/hadoop/Documents/5.3.treesinfo/reducer1.py" -reducer "python3 /home/hadoop/Documents/5.3.treesinfo/reducer1.py" \
-input /test/input/* -output /test/output1

echo "2nd MapReduce: compute the height of the heightest tree of each type ..."
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.3.treesinfo/mapper2.py" -mapper "python3 /home/hadoop/Documents/5.3.treesinfo/mapper2.py" \
-file "/home/hadoop/Documents/5.3.treesinfo/reducer2.py" -reducer "python3 /home/hadoop/Documents/5.3.treesinfo/reducer2.py" \
-input /test/input/* -output /test/output2

echo "3rd MapReduce: compute the borough (arrondi) of the oldest tree in Paris ..."
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.3.treesinfo/mapper3.py" -mapper "python3 /home/hadoop/Documents/5.3.treesinfo/mapper3.py" \
-file "/home/hadoop/Documents/5.3.treesinfo/reducer3.py" -reducer "python3 /home/hadoop/Documents/5.3.treesinfo/reducer3.py" \
-input /test/input/* -output /test/output3

echo "------------ MapReduce done ------------"

/usr/local/hadoop/bin/hadoop fs -ls /test
/usr/local/hadoop/bin/hadoop fs -copyToLocal /test/output1/* /home/hadoop/Documents/5.3.treesinfo/output1
/usr/local/hadoop/bin/hadoop fs -copyToLocal /test/output2/* /home/hadoop/Documents/5.3.treesinfo/output2
/usr/local/hadoop/bin/hadoop fs -copyToLocal /test/output3/* /home/hadoop/Documents/5.3.treesinfo/output3

