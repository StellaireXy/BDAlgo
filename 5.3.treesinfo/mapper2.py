#Compute the height of the highest tree of each type
#Mapper2
#IN:  arbres.csv
#OUT: type height \t 1

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
    hauteur = info_tree[6]
    #circonf = info_tree[7]
    #adresse = info_tree[8]
    #commun = info_tree[9]
    #variete = info_tree[10]
    #obj = info_tree[11]
    #nom_ev = info_tree[12][0:-2]
    
    if n != 0 and len(hauteur) > 0 and len(genre) > 0:
        h = float(hauteur)
        hei = '%.2f' %h
        l = len(hei)
        height = '0'*(3 - l) + hei
        type_height = genre + ' ' + hei
        print("%s\t%s" % (type_height, '1'))
    
    n += 1
