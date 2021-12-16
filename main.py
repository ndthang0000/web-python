# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
from source import test


app=Flask(__name__)

@app.route('/',methods=["GET"])
def get_index():
    word = request.args.get('word', type=str, default='')
    data, frequency = test.count_occurence(word)
    matrix_occurence=test.co_occurence(word)
    print(matrix_occurence)
    return render_template('index.html', data=data, word=word, frequency=frequency,matrix_occurence=matrix_occurence)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
