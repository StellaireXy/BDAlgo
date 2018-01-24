#!/bin/bash
# This shell is to run 5.1 MapReduce

echo "Copy the input files from local to HDFS"
/usr/local/hadoop/bin/hadoop fs -mkdir /test
/usr/local/hadoop/bin/hadoop fs -mkdir /test/input
/usr/local/hadoop/bin/hadoop fs -copyFromLocal /home/hadoop/Documents/5.1.tfidf/input/defoe-robinson-103.txt /test/input
/usr/local/hadoop/bin/hadoop fs -copyFromLocal /home/hadoop/Documents/5.1.tfidf/input/callwild /test/input

echo "Run the 1st round MapReduce"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.1.tfidf/mapper1.py" -mapper "python3 /home/hadoop/Documents/5.1.tfidf/mapper1.py" \
-file "/home/hadoop/Documents/5.1.tfidf/reducer1.py" -reducer "python3 /home/hadoop/Documents/5.1.tfidf/reducer1.py" \
-input /test/input/* -output /test/output1

echo "Run the 2nd round MapReduce"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.1.tfidf/mapper2.py" -mapper "python3 /home/hadoop/Documents/5.1.tfidf/mapper2.py" \
-file "/home/hadoop/Documents/5.1.tfidf/reducer2.py" -reducer "python3 /home/hadoop/Documents/5.1.tfidf/reducer2.py" \
-input /test/output1/* -output /test/output2

echo "Run the 3rd round MapReduce"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.1.tfidf/mapper3.py" -mapper "python3 /home/hadoop/Documents/5.1.tfidf/mapper3.py" \
-file "/home/hadoop/Documents/5.1.tfidf/reducer3.py" -reducer "python3 /home/hadoop/Documents/5.1.tfidf/reducer3.py" \
-input /test/output2/* -output /test/output3

echo "Get the final TF-IDF output and sort by TF-IDF"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.1.tfidf/mapper_sort.py" -mapper "python3 /home/hadoop/Documents/5.1.tfidf/mapper_sort.py" \
-file "/home/hadoop/Documents/5.1.tfidf/reducer_sort.py" -reducer "python3 /home/hadoop/Documents/5.1.tfidf/reducer_sort.py" \
-input /test/output3/* -output /test/output

echo "------------------ MapReduce finished ------------------"
/usr/local/hadoop/bin/hadoop fs -ls /test/output/
/usr/local/hadoop/bin/hadoop fs -copyToLocal /test/output/part-00000 /home/hadoop/Documents/5.1.tfidf/output
