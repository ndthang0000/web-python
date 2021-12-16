with open('source/data.txt', 'r', encoding='utf-8') as f:
    data_train=f.readlines()
with open('source/label.txt', 'r', encoding='utf-8') as f:
    label_train=f.readlines()

V=[]
for i in data_train:
    for j in i.split(' '):
        V.append(j.lower())
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
word_to_occurence={i:count(i,V) for i in Vocab}

