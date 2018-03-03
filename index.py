

'''

Index structure:

    The Index class contains a list of IndexItems, stored in a dictionary type for easier access

    each IndexItem contains the term and a set of PostingItems

    each PostingItem contains a document ID and a list of positions that the term occurs

'''

import doc
from util import *

class Posting:
    def __init__(self, docID):
        self.docID = docID
        self.positions = []

    def append(self, pos):
        self.positions.append(pos)
        #print('doc is '+str(self.docID)+'positions list'+str(self.positions))
    def sort(self):
        ''' sort positions'''
        self.positions.sort()

    def merge(self, positions):
        self.positions.extend(positions)

    def term_freq(self):
        ''' return the  term frequency in the document'''
        #ToDo



class IndexItem:
    def __init__(self, term):
        self.term = term
        self.posting = {} #postings are stored in a python dict for easier index building
        self.sorted_postings= [] # may sort them by docID for easier query processing

    def add(self, docid, pos):
        ''' add a posting'''

        if not self.posting.has_key(docid):
            self.posting[docid] = Posting(docid)
        self.posting[docid].append(pos)

        #print(self.posting)

    def sort(self):
        ''' sort by document ID for more efficient merging. For each document also sort the positions'''
        # ToDo



class InvertedIndex:

    def __init__(self):
        self.items = {} # list of IndexItems
        self.nDocs = 0  # the number of indexed documents


    def indexDoc(self, doc):
        # indexing a Document object
        ''' indexing a docuemnt, using the simple SPIMI algorithm, but no need to store blocks due to the small collection we are handling. Using save/load the whole index instead'''

        # ToDo: indexing only title and body; use some functions defined in util.py
        # (1) convert to lower cases,
        # (2) remove stopwords,
        # (3) stemming

        after_prepro = preprocessing_txt(doc.body)

        for term in set(after_prepro):
                if term in self.items.keys():
                    pos=getPositions(term,after_prepro)
                    #print("position got in IFPART for "+term+" is "+str(pos)+" in the documents "+doc.docID)
                    self.items[term].add(int(doc.docID),pos)
                    print("term is ----- "+str(term)+" ------present in the docs ------"+str(self.items[term].posting.keys()))
                    for k in range(0, 1401, 1):
                     if k in self.items[term].posting.keys():
                       print("       and its positions are -----"+str(self.items[term].posting[k].positions))
                    #print('name of the term and objest is already created:'+str(term)+"and all the docs it is in :"+str(self.items[term].posting.keys()))#+'positions in the list is:'+str(self.items[term].posting[doc.docID].positions))
                else:
                    obj_Index_item=IndexItem(term)
                    pos=getPositions(term,after_prepro)
                    #print("position got in elsePART for " + term + " is " + str(pos) + " in the documents " + doc.docID)
                    obj_Index_item.add(int(doc.docID),pos)
                    self.items[term] =obj_Index_item
                    print("term is ----- " + str(term) + "----- present in the docs ------" + str(self.items[term].posting.keys()))
                    for k in range(0,1401,1):
                        if k in self.items[term].posting.keys():
                           print("----- and its positions are -----"+str(self.items[term].posting[k].positions))
                    #print("name of the term is:"+str(term)+" and all the documents it is in "+str(self.items[term].posting.keys()))#+"position list is:"+str(self.items[term].posting[doc.docID].positions))

    def sort(self):
        ''' sort all posting lists by docID'''
        #ToDo

    def find(self, term):
        return self.items[term]

    def save(self, filename):
        ''' save to disk'''
        # ToDo: using your preferred method to serialize/deserialize the index

    def load(self, filename):
        ''' load from disk'''
        # ToDo

    def idf(self, term):
        ''' compute the inverted document frequency for a given term'''
        #ToDo: return the IDF of the term

    # more methods if needed


def test():
    ''' test your code thoroughly. put the testing cases here'''
    print 'Pass'

def indexingCranfield():
    #ToDo: indexing the Cranfield dataset and save the index to a file
    # command line usage: "python index.py cran.all index_file"
    # the index is saved to index_file

    print 'Done'

def getPositions(term,after_prepro):
    index=1
    positions=[]
    for each_term in after_prepro:
        if term==each_term:
            positions.append(index)
            index=index+1
        else:
            index=index+1
    return positions


if __name__ == '__main__':
    #test()
    indexingCranfield()
