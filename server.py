from flask import Flask, render_template, request
from tinydb import TinyDB
import requests

app = Flask(__name__)

db = TinyDB('assets/database.json')
table = db.table('table')


def api_call(country_code):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = (requests.get(url))
    data = response.json()
    price = data['bpi'][country_code]['rate']
    table.insert({'price': price})
    return str(price)


@app.route('/')
def index_route():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index_post_route():
    return render_template('index.html',
                           message=api_call(request.form['text']))


if __name__ == "__main__":
    app.run(port=3000)
