from pyvi import ViTokenizer

with open('source/data.txt','r',encoding='utf-8') as f:
    data_train=f.readlines()
with open('source/label.txt','r',encoding='utf-8') as f:
    label_train=f.readlines()

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
        return 0,0
    try:
        word=ViTokenizer.tokenize(word)
        print(word)
        if len(word.split())>1:
            return -1,-1
        return word_to_occurence[word], round(word_to_occurence[word]/len(data_train)*100,3)
    except:
        return 0, 0
def co_occurence(word):
    if word=='':
        return []
    try:
        matrix_occurence=[]
        word_occurence=[]
        word = ViTokenizer.tokenize(word)
        if len(word.split()) > 1:
            return []
        for i in Matrix:
            if word_to_index[word] in i:
                index=Matrix.index(i)
                word_occurence.append(data_train[index])
                for j in i:
                    if j==word:
                        continue
                    matrix_occurence.append(j)



        return word_occurence
    except:
        return []
