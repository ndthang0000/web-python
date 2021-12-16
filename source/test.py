from pyvi import ViTokenizer
import numpy as np
with open('source/data.txt','r',encoding='utf-8') as f:
    data_train=f.readlines()
with open('source/label.txt','r',encoding='utf-8') as f:
    label_train=f.readlines()

word_to_type={
    "NN":0,
    "NC":1,
    "NP":2,
    "VP":3,
    "JJ":4,
    "PP":5,
    "D":6,
    "AD":7,
    "IN":8,
    "CC":9,
    "UH":10,
    "RB":11,
    "X":12,
    "Symbol":13
}
V=[]
Matrix=[]
for i in data_train:
    for j in i.split():
        V.append(j)
Vocab = list(set(V))

def count(word,V):
    result=0
    for i in V:
        if i==word:
            result+=1
    return result 
word_to_index = {w : (i+2) for i, w in enumerate(Vocab)}
word_to_index['UNK'] = 1
word_to_index['PAD'] = 0
index_to_word = {i: w for w, i in word_to_index.items()}

word_to_occurence={i:count(i,V) for i in Vocab}

for i in data_train:
    temp=[]
    for j in i.split():
        temp.append(word_to_index[j])
    Matrix.append(temp)


def count_occurence(word):
    if word=='':
        return 0,0,''
    try:
        word=ViTokenizer.tokenize(word).strip()
        print(word)
        if len(word.split())>1:
            return -1,-1,''
        return word_to_occurence[word], round(word_to_occurence[word]/len(data_train)*100,3), word
    except:
        return 0, 0,''
def co_occurence(word):
    if word=='':
        return [],[]
    try:
        word_occurence=[]
        arr_type = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=int)
        word = ViTokenizer.tokenize(word).strip()
        if len(word.split()) > 1:
            return [],[]
        for i in Matrix:
            if word_to_index[word] in i:
                index_line=Matrix.index(i)  #index line
                index_word=i.index(word_to_index[word]) #index word
                word_occurence.append(data_train[index_line])
                print(index_line)
                try :
                    arr_type[word_to_type[label_train[index_line].split()[index_word]]]+=1
                except:
                    pass





        return word_occurence,arr_type
    except:
        return [],[]
