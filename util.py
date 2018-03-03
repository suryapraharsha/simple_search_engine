
'''
   utility functions for processing terms

    shared by both indexing and query processing
'''
import nltk
import re
stopword_list=[]

def isStopWord(word):
    ''' using the NLTK functions, return true/false'''

    stopwords = open('stopwords', 'r')
    for word_ST in stopwords:
        stopword_list.append(word_ST.strip('\n'))

        if word in stopword_list:
           return True
        else:
           return False



def stemming(word):
    ''' return the stem, using a NLTK stemmer. check the project description for installing and using it'''
    stemmer = nltk.stem.porter.PorterStemmer()
    after_stemming_word=stemmer.stem(word)
    return after_stemming_word
    # ToDo


def tokenizer(text):
    text = re.sub("[^a-zA-Z]+", " ", text)
    tokens = nltk.tokenize.word_tokenize(text)
    return tokens


def preprocessing_txt(text):
    final_tokens = []
    tokens = tokenizer(text)
    stemmer = nltk.stem.porter.PorterStemmer()

    new_text = ""
    for token in tokens:
        token = token.lower()
        if token not in open('stopwords').read():
            #             print token
            new_text += stemmer.stem(token)
            new_text += " "

    final_tokens=new_text.split(" ")
    return final_tokens
