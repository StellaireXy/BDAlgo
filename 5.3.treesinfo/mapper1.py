#Compute the number of trees by type
#Mapper1
#IN:  arbres.csv
#OUT: type \t 1

import sys

n = 0

for line in sys.stdin:
    
    info_tree = line.strip().split(';')
    
    #geo_point = info_tree[0]
    #arrondi = info_tree[1]
    genre = info_tree[2]
    #espace = info_tree[3]
    #famille = info_tree[4]
    #annee = info_tree[5]
    #hauteur = info_tree[6]
    #circonf = info_tree[7]
    #adresse = info_tree[8]
    #commun = info_tree[9]
    #variete = info_tree[10]
    #obj = info_tree[11]
    #nom_ev = info_tree[12][0:-2]
    if n != 0:
        print("%s\t%s" % (genre, '1'))
    
    n += 1
