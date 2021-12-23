# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
from source import test


app=Flask(__name__)

@app.route('/',methods=["GET"])
def get_index():
    word = request.args.get('word', type=str, default='')
    data, frequency,word_segment = test.count_occurence(word)
    sentences_occurence, arr_type =test.co_occurence(word)
    return render_template('index.html', data=data, word=word,word_segment=word_segment, frequency=frequency,matrix_occurence=sentences_occurence,arr_type=arr_type )

# @app.route('/statistic',methods=["GET"])
# def statistic():
#     return render_template('statistic.html')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
