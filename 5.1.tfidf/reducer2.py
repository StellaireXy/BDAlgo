#Round2
#reducer2
#IN:  doc \t word count
#OUT: word doc \t count wordsPerDoc

import sys

pre_doc = None
cur_count = 0
word = None
wPD = 0
dic_doc = {}
l = []

for line in sys.stdin:
    nline = line.strip()
    l.append(nline)
    doc, wordcount = nline.split('\t', 1)
    word, count = wordcount.split(' ', 1)
    count = int(count)
    if pre_doc == doc:
        wPD += count
    else:
       if pre_doc != None:
            dic_doc[pre_doc] = wPD
       wPD = 0
       pre_doc = doc
dic_doc[pre_doc] = wPD

for li in l:
    doc, wordcount = li.split('\t', 1)
    word, count = wordcount.split(' ', 1)
    
    for k in dic_doc:
        if doc == k:
           worddoc = word + ' ' + doc
           countwPD = count + ' ' + str(dic_doc[doc])
           print("%s\t%s" % (worddoc, countwPD))
    
