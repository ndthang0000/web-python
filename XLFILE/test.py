import re

with open('dev.txt', 'r',encoding='utf-8') as f:
    data = f.readlines()
line=''
label=''
for i in range(0,len(data)):
    if data[i].split('\n')[0]=='':
        continue
    test=data[i].split('\n')[0].split(' ')
    temp_line=''
    temp_label=''
    for j in test:
        try:
            word_temp=j.split('//')
            if len(word_temp)>2:
                temp_line+=word_temp[0]+word_temp[1]+' '
                temp_label+=word_temp[2]+' '
            else:
                temp_line+=word_temp[0]+' '
                temp_label+=word_temp[1]+' '
        except:
            pass
    line+=re.sub(r'\W+', ' ', temp_line).lower().lstrip()+'\n'
    label+=re.sub(r'\W+', ' ', temp_label).lstrip()+'\n'

with open('data.txt', 'a+',encoding='utf-8') as f:
    f.write(line)
with open('label.txt', 'a+',encoding='utf-8') as f:
    f.write(label)