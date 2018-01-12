from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_redis import FlaskRedis
from DB_Access import *

app = Flask(__name__)
redis_store = FlaskRedis(app)

@app.route("/", methods=['GET', 'POST'])
def orderPage():
    if request.method == 'POST':
        insert_in_orders([request.form['phoneNumber'], request.form['Adress']])

    return render_template('main.html')

@app.route("/login", methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET' and isLogged(request):
        return redirect('/admin')

    if request.method == 'POST':
        result = find_user(request.form['login'], request.form['password'])
        if not result:
            print("User not found")
            return make_response('User not found')
        else:
            #return render_template('orders_page.html', orders=_orders)
            resp = make_response(redirect('/admin'))
            resp.set_cookie('username', request.form['login'])
            redis_store.setex(request.form['login'], 60, request.form['login'])
            return resp

    return render_template('login_page.html')

@app.route("/admin")
def orderListPage():
    if request.method == 'POST':
        redis_store.delete(request.cookies.get('username'))

    if request.method == 'GET' and isLogged(request):
        _orders = find_orders()
        if isAdmin(request):
            return render_template('orders_page.html', orders=_orders)
        return render_template('orders_page.html')
    else:
        return redirect('/login')

@app.route("/logout")
def logout():
    redis_store.delete(request.cookies.get('username'))
    return redirect('/')

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


def isLogged(request):
    try:
        username = request.cookies.get('username')
        if redis_store.get(username).decode("utf-8")  == username:
            return True
    except:
        print("Not logged")

    return False


if __name__ == "__main__":
    #REDIS_URL = "redis://:password@localhost:6379/0"

    app.config['DEBUG'] = True
    app.run(port=8000)
