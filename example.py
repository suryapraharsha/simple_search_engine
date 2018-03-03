class Posting:
    def __init__(self, docID):
        self.docID = docID
        self.positions = []
    def append(self, pos):
        self.positions.append(pos)
    def merge(self, positions):
        self.positions.extend(positions)

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

class InvertedIndex:

    def __init__(self):
        self.items = {} # list of IndexItems
        self.nDocs = 0  # the number of indexed documents

p1=Posting(444)
p1.positions=[2,3,4,5]

p2=Posting(445)
p2.append(1)
p4=Posting(444)
p4.positions=[10,11,12]
p3=Posting(555)
p4.append(13)




i1=IndexItem("surya")
i2=IndexItem("charan")

i3=IndexItem("vinay")
i3.posting[444]=p3.positions
i3.add(444,p4.positions)

i1.posting[444]=p1.positions
i1.posting[777]=p1.positions


i2.posting[p2.docID]=p2.positions
i2.posting[666]=p1.positions
#print(p3.positions)
i3.add(p3.docID,p3.positions)

I=InvertedIndex()

I.items[i1.term]=i1.posting
I.items[i2.term]=i2.posting
I.items[i3.term]=i3.posting
print I.items

print(len(I.items))
print(I.items.has_key('vinay'))

key=I.items.iterkeys()
for i in range(len(I.items)):
    print(key.next())
#print vars(i2)

objs_posting = [Posting for i in range(5)]
objs_posting[0]=Posting(1)
objs_posting[0].positions=[1,2,3]
objs_posting[1].positions=[4,5,6]
objs_posting[2].positions=[7,8,9]
objs_posting[3].positions=[4,6,8]
objs_posting[4].positions=[1,3,5]

for i in range(5):
    print(objs_posting[i].positions)

objs_indexitems=[IndexItem for i in range(len(after_prepro))]

