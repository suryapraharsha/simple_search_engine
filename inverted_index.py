from cran import *
import nltk
import re
import util
import index


cf = CranFile ('cran.all')




'''for each_term in after_prepro:

        each_term_position=getPositions(each_term,after_prepro)
        print(each_term_position)
        i=1'''
n=0
I=InvertedIndex()
for i in cf.docs:
    if n==15:
        break
    else:
        I.indexDoc(i)
        n=n+1

final_dict={}

'''for i in range(len(I.items)):
    final_dict[I[i].items]=
'''







