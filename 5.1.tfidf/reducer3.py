#Round3
#reducer3
#IN:  word \t doc count wordsPerDoc 1
#OUT: word doc \t count wordsPerDoc docsPerWord

import sys

pre_word = None
dPW = 1 
word = None
dic_word = {}
l = []

for line in sys.stdin:

    word, doccountwPDdPW = line.strip().split('\t', 1)
    doc, count, wPD, c = doccountwPDdPW.split(' ',3)

    if pre_word == word:
        dPW = dPW + int(c)
    else:
        if pre_word != None:
            countwPDdPW = count + ' ' + wPD + ' ' + str(dPW)
            dic_word[pre_word] = countwPDdPW
            worddoc = pre_word + ' ' + doc
            l.append(worddoc)
        dPW = 1
        pre_word = word
     
countwPDdPW = count + ' ' + wPD + ' ' + str(dPW)
dic_word[pre_word] = countwPDdPW
worddoc = pre_word + ' ' + doc
l.append(worddoc)

for line in l:
    word, doc = line.split(' ',1)
    for d in dic_word:
        if word == d:
            print("%s\t%s" % (line, dic_word[word]))

