from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/<item>')
def get_item_page(item):
    for i in get_data():
        if i['title'] == item:
            return render_template("item.html",
                                   title=i['title'],
                                   text=i['text'],
                                   image=i['title'] + '.jpg',
                                   count=len(i['text'].split()))
    return render_template("home.html")


@app.route('/author')
def get_author_page():
    return render_template('author.html')


if __name__ == "__main__":
    app.run(debug=True)
