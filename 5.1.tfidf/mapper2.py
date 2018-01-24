#Round2
#mapper2
#IN:  word doc \t count
#OUT: doc \t word count

import sys

for line in sys.stdin:

    worddoc, count = line.strip().split('\t',1)
    word, doc = worddoc.split(' ',1)
    wordcount = word + ' ' + count
    print("%s\t%s" % (doc, wordcount))
        
