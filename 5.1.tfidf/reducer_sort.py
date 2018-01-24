#Sort by Shuffle
#reducer_sort
#IN:  TF-IDF \t word doc
#OUT: word doc \t TF-IDF

import sys

for line in sys.stdin:

    tfidf, worddoc = line.strip().split('\t', 1)
    ti = 1 - float(tfidf)
    t = '%.20f' %ti
    print("%s\t%s" % (worddoc, t))

