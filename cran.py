'''

processing the special format used by the Cranfield Dataset



'''
from doc import Document
import nltk
import re
from index import *

class CranFile:
    def __init__(self, filename):
        self.docs = []

        cf = open(filename)
        docid = ''
        title = ''
        author = ''
        body = ''

        for line in cf:
            if '.I' in line:
                if docid != '':
                    body = buf
                    self.docs.append(Document(docid, title, author, body))
                # start a new document
                docid = line.strip().split()[1]
                buf = ''
            elif '.T' in line:
                None
            elif '.A' in line:
                title = buf # got title
                buf = ''
            elif '.B' in line:
                author = buf # got author
                buf = ''
            elif '.W' in line:
                buf = '' # skip affiliation
            else:
                buf += line


def tokenizer(text):
    text = re.sub("[^a-zA-Z]+", " ", text)
    tokens = nltk.tokenize.word_tokenize(text)
    return tokens


def preprocessing_txt(text):
    tokens = tokenizer(text)
    stemmer = nltk.stem.porter.PorterStemmer()
    #stopwords = nltk.corpus.stopwords.words('english')
    new_text = ""
    for token in tokens:
        token = token.lower()
        if token not in open('stopwords').read():
            #             print token
            new_text += stemmer.stem(token)
            new_text += " "

    return new_text

if __name__ == '__main__':
    ''' testing '''

    cf = CranFile('cran.all')
    for doc in cf.docs:
        #print ("docId="+doc.docID),("title="+doc.title),("author="+doc.author),("body="+doc.body)
        '''print("tokensof "+str(int(doc.docID)+int("1"))+" are ==========")
        print(tokenizer(doc.body))
        print("after prepr")
        final_tokens=preprocessing_txt(doc.body).split(" ")
        print(final_tokens)

        #index_list = [] means inverted index InvertedIndex.items()

        doc_info = {}
        for i in range(len(final_tokens)):
            pos = i + 1
            word = final_tokens[i]
            index_found = 0
            for index in range(len(InvertedIndex.items)):
                if InvertedIndex.items[index][0] == word:
                    IndexItem = InvertedIndex.items[index][1]
                    item.append([str(doc_id), pos])
                    index_list[index][1] = item
                    index_found = 1
                    break
            if index_found == 0:
                index_list.append([word, [[str(doc_id), pos]]])
            doc_info[doc_id] = (doc_num, doc_size)'''

