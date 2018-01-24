#Round1
#mapper1
#IN:  2 docs
#OUT: word doc \t 1

import sys
import os

stop_words =  ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it',
               'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
               'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
               'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
               'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'more', 'other', 'some', 'such', 'no', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
               'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma',
               'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', "'s", "'m", "'t", "'ll", "n't", "'ve", "''", '``', "'re"]

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

for line in sys.stdin:
    
    doc = os.environ["map_input_file"]
    
    words = line.strip().lower().split()
    
    for word in words:
        if (len(word) >= 1) and (word[0] in punctuation):
            word = word[1:]
        if (len(word) >= 1) and (word[-1] in punctuation):
            word = word[0:-1]
        if (len(word) >= 1) and (word[0] in punctuation):
            word = word[1:]
        if (len(word) >= 1) and (word[-1] in punctuation):
            word = word[0:-1]
        if (len(word) >= 1) and (word not in stop_words) and (word not in punctuation):
            z = word + ' ' +  doc
            print("%s\t%s" % (z, "1"))

