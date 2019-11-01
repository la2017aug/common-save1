from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)

data=get_data()


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/author')
def get_author_page():
    return render_template('author.html')


@app.route('/alarm_clock')
def get_alarm_page():
    return render_template('alarm_clock.html', data)


@app.route('/headphones')
def get_headphones_page():
    return render_template('headphones.html', data)


@app.route('/ipod')
def get_ipod_page():
    return render_template('ipod.html', data)


@app.route('/calculator')
def get_calculator_page():
    return render_template('calculator.html', data)


@app.route('/coffeemaker')
def get_coffeemaker_page():
    return render_template('coffeemaker.html', data)


@app.route('/battery_charger')
def get_charger_page():
    return render_template('battery_charger.html', data)


if __name__ == "__main__":
    app.run(debug=True)
