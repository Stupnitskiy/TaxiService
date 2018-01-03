from flask import Flask, render_template, request
from jinja2 import Template
from DB_Access import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def orderPage():
    if request.method == 'POST':
        insert_in_orders([request.form['phoneNumber'], request.form['Adress']])

    return render_template('main.html')

@app.route("/orders", methods=['GET', 'POST'])
def orderListPage():
    if request.method == 'POST':
        result = find_user(request.form['login'], request.form['password'])
        if not result:
            print("User not found")
        else:
            _orders = find_orders()
            return render_template('orders_page.html', orders=_orders)

    return render_template('login_page.html')

@app.route("/yes")
def yes():
    return "yes"

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(port=8000)
