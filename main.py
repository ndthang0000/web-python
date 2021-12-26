# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
from source import data


app=Flask(__name__)

@app.route('/',methods=["GET"])
def get_index():
    word = request.args.get('word', type=str, default='')
    data_, frequency,word_segment = data.count_occurence(word)
    sentences_occurence, arr_type = data.co_occurence(word)
    return render_template('index.html', data=data_, word=word,word_segment=word_segment, frequency=frequency,matrix_occurence=sentences_occurence,arr_type=arr_type )

@app.route('/statistic',methods=["GET"])
def statistic():
    quantity_word, quantity_sentence, top_word = data.statistic()
    print(top_word)
    print(top_word[0][0])
    return render_template('statistic.html',quantity_word=quantity_word,quantity_sentence=quantity_sentence,top_word=top_word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
