#Compute TF-IDF
#mapper_sort
#IN:  word doc \t count wordsPerDoc docsPerWord
#OUT: TF-IDF \t word doc

import sys
from math import log10, sqrt

totalDocs = 2.0

for line in sys.stdin:

    line = line.strip()

    worddoc, countwPDdPW = line.strip().split('\t',1)
    count, wPD, dPW = countwPDdPW.split(' ',2)
    count = float(count)
    wPD = float(wPD)
    dPW = float(dPW)
    tfidf = 1- (count/wPD) * log10(totalDocs/dPW)
    t = '%.20f' %tfidf
    print("%s\t%s" % (t, worddoc))
        
