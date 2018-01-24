#Round3
#mapper3
#IN:  word doc \t count wordsPerDoc
#OUT: word \t doc count wordsPerDoc 1

import sys

for line in sys.stdin:

    worddoc, countwPD = line.strip().split('\t',1)
    word, doc = worddoc.split(' ',1)
    doccountwPD = doc + ' ' + countwPD + ' ' + str(1)
    print("%s\t%s" % (word, doccountwPD))
        
