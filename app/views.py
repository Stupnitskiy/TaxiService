from flask import render_template, request, make_response, redirect
from app import app, redis_store, session
from app.models import User, Order



@app.route("/", methods=['POST'])
def orderAdd():

    new_order = Order(request.form['phoneNumber'], request.form['Adress'])
    session.add(new_order)
    return render_template('order.html')


@app.route("/", methods=['GET'])
def orderPage():

    return render_template('order.html')


@app.route("/login", methods=['POST'])
def logginIn():

    user = session.query(User).filter_by(login=request.form['login'], \
    password=request.form['password']).first()
    if not user:
        print("User not found")
    else:
        #return render_template('orders_page.html', orders=_orders)
        resp = make_response(redirect('/admin'))
        resp.set_cookie('username', request.form['login'])
        redis_store.setex(request.form['login'], 60, request.form['login'])
        return resp

    return redirect('/admin')


@app.route("/login", methods=['GET'])
def loginPage():

    if isLogged(request):
        return redirect('/admin')
    return render_template('login.html')


@app.route("/admin")
def orderListPage():

    if isLogged(request):
        listOfOrders = []
        orders = session.query(Order).all()
        for order in orders:
            listOfOrders.append([order.id, order.number, order.destination])

        if isAdmin(request):
            return render_template('admin.html', orders=listOfOrders)
        return render_template('admin.html')
    else:
        return redirect('/login')


@app.route("/logout")
def logout():

    redis_store.delete(request.cookies.get('username'))
    return redirect('/')


def isLogged(request):

    try:
        username = request.cookies.get('username')
        if redis_store.get(username).decode("utf-8")  == username:
            return True
    except:
        print("Not logged")

    return False


def isAdmin(request):

    username = request.cookies.get('username')
    user = session.query(User).filter_by(login=username, isadmin=True)\
    .first()



    if user is None:
        print('not isAdmin')
        return False
    print('isAdmin')
    return True
