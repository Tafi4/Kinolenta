from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/water')
def water():
    return render_template('water.html')


if __name__ == '__main__':
    app.run()
