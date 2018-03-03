text="experimental investigation of the aerodynamics of a wing in a slipstream .an experimental study of a wing in a propeller slipstream was made in order to determine the spanwise distribution of the lift increase due to slipstream at different angles of attack of the wing and at different free stream to slipstream velocity ratios .  theresults were intended in part as an evaluation basis for different theoretical treatments of this problem . the comparative span loading curves, together withsupporting evidence, showed that a substantial part of the lift incrementproduced by the slipstream was due to a /destalling/ or boundary-layer-control effect .  the integrated remaining lift increment, after subtracting this destalling lift, was found to agree well with a potential flow theory .an empirical evaluation of the destalling effects was made forthe specific configuration of the experiment ."
doc_id=1
import re
import nltk

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
    final_tokens=preprocessing_txt(text).split(" ")

    index_list = []

    for i in range(len(final_tokens)):
        pos = i + 1
        word = final_tokens[i]
        index_found = 0
        for x in range(len(index_list)):
            if index_list[x][0] == word:
                print index_list[x][0]
                item = index_list[x][1]
                item.append([str(doc_id), pos])
                index_list[x][1] = item
                index_found = 1
                break
        if index_found == 0:
            index_list.append([word, [[str(doc_id), pos]]])

    #print("\nindex is")
    #print(index_list[i][0] for i in range(len(index_list)))
    print(index_list)
'''
[
 ["red",[["D1",1], ["D1", 2], ["D1", 5], ["D2", 2]]],
 ["blue", [["D1", 4]]], ["black", [["D1", 4]]],
 ["white", [["D2", 1], ["D2", 3], ["D2", 4]]]
]

[
    [u'experiment', [['1', 1]]],
    [u'investig', [['1', 2]]],
    [u'aerodynam', [['1', 3]]],
    [u'wing', [['1', 4]]],
    [u'slipstream', [['1', 5]]]
]

[
    [u'experiment', [  ['1', 1]   ,   ['1', 6]  ]         ],

    [u'investig', [['1', 2]]],

    [u'aerodynam', [['1', 3]]],

    [u'wing', [['1', 4]]],

    [u'slipstream', [['1', 5]]],

    [u'studi', [['1', 7]]]
]'''