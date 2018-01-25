#!bin/bash
# This shell is to run 5.2 MapReduce

echo "Copy the input file from local"
/usr/local/hadoop/bin/hadoop fs -rm -r /test
/usr/local/hadoop/bin/hadoop fs -mkdir /test
/usr/local/hadoop/bin/hadoop fs -mkdir /test/input
/usr/local/hadoop/bin/hadoop fs -copyFromLocal /home/hadoop/Documents/5.2.pagerank/input/soc-Epinions1.txt /test/input

echo "Run the initializer"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.2.pagerank/Initializer.py" -mapper "python3 /home/hadoop/Documents/5.2.pagerank/Initializer.py" \
-numReduceTasks 0 \
-input /test/input/soc-Epinions1.txt -output /test/output1

echo "Run the MapReduce 40 times"

for ((i=1; i<=40; i++)); do
    
    echo "$i iteration starts ..."
    
    j=$[$i+1]
    /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
    -file "/home/hadoop/Documents/5.2.pagerank/mapper.py" -mapper "python3 /home/hadoop/Documents/5.2.pagerank/mapper.py" \
    -file "/home/hadoop/Documents/5.2.pagerank/reducer.py" -reducer "python3 /home/hadoop/Documents/5.2.pagerank/reducer.py" \
    -input /test/output$i/* -output /test/output$j
    
done

echo "Run the mapper with a last special reducer"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.2.pagerank/mapper.py" -mapper "python3 /home/hadoop/Documents/5.2.pagerank/mapper.py" \
-file "/home/hadoop/Documents/5.2.pagerank/reducer_last.py" -reducer "python3 /home/hadoop/Documents/5.2.pagerank/reducer_last.py" \
-input /test/output41/* -output /test/output42

echo "Sort the nodes by pagerank"
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar \
-file "/home/hadoop/Documents/5.2.pagerank/mapper_sort.py" -mapper "python3 /home/hadoop/Documents/5.2.pagerank/mapper_sort.py" \
-file "/home/hadoop/Documents/5.2.pagerank/reducer_sort.py" -reducer "python3 /home/hadoop/Documents/5.2.pagerank/reducer_sort.py" \
-input /test/output42/* -output /test/output

echo "------------ MapReduce done ------------"

/usr/local/hadoop/bin/hadoop fs -ls /test/output
/usr/local/hadoop/bin/hadoop fs -copyToLocal /test/output/* /home/hadoop/Documents/5.2.pagerank/output

