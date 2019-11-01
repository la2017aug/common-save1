from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/author')
def get_author_page():
    return render_template('author.html')


@app.route('/alarm_clock')
def get_alarm_page():
    title = "Alarm clock"
    img_url = "alarm_clock.jpg"
    return render_template("alarm_clock.html", data=get_data(), title=title, img_url=img_url)


@app.route('/headphones')
def get_headphones_page():
    title = "Alarm clock"
    img_url = "alarm_clock.jpg"
    return render_template('headphones.html', data=get_data(), title=title, img_url=img_url)


@app.route('/ipod')
def get_ipod_page():
    title = "Alarm clock"
    img_url = "alarm_clock.jpg"
    return render_template('ipod.html', data=get_data(), title=title, img_url=img_url)


@app.route('/calculator')
def get_calculator_page():
    title = "Calculator"
    img_url = "Calculator.jpg"
    return render_template('calculator.html', data=get_data(), title=title, img_url=img_url)


@app.route('/coffeemaker')
def get_coffeemaker_page():
    title = "Coffeemaker"
    img_url = "coffeemaker.jpg"
    return render_template('coffeemaker.html', data=get_data(), title=title, img_url=img_url)


@app.route('/battery_charger')
def get_charger_page():
    title = "Battery charger"
    img_url = "battery_charger.jpg"
    return render_template('battery_charger.html', data=get_data(), title=title, img_url=img_url)


if __name__ == "__main__":
    app.run(debug=True)
