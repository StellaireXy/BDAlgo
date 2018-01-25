#Computer the borough (arrondi) of the oldest tree in Paris
#Reducer3
#OUT: oldest \t borough

import sys

oldest = -1
ls_borough = []

for line in sys.stdin:
    
    year, arrondi = line.strip().split('\t', 1)
    
    old = 2018 - int(year)
    
    if old == oldest:
        ls_borough += [arrondi]
    elif old > oldest:
        oldest = old
        ls_borough = [arrondi]

for borough in ls_borough:
    print("%s\t%s" % (str(oldest), borough))
