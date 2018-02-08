from flask import render_template, request, make_response, redirect, session
from flask.views import MethodView
from app import app, redis_store
from app.models import User, Order
import app.controller as ctr


class OrderAPI(MethodView):

    def get(self):
        return render_template('order.html')

    def post(self):
        ctr.order_add(request.form['phoneNumber'], request.form['Adress'])
        return redirect('/')

order_view = OrderAPI.as_view('order_api')
app.add_url_rule('/', view_func=order_view, methods=['GET'])
app.add_url_rule('/api/order/add', view_func=order_view, methods=['POST'])


@app.route("/login", methods=['POST'])
def login():

    user = ctr.get_user(request.form['login'], request.form['password'])
    if not user:
        return redirect('/login')

    session['username'] = request.form['login']
    redis_store.setex(request.form['login'], 60, request.form['login'])
    return redirect('/admin')


@app.route("/login", methods=['GET'])
def login_page():

    if is_logged(request):
        return redirect('/admin')
    return render_template('login.html')


@app.route("/admin")
def orderlist_page():

    if is_logged(request):
        list_of_orders = ctr.get_orders()

        if is_admin(request):
            return render_template('admin.html', orders=list_of_orders)
        return render_template('admin.html')
    else:
        return redirect('/login')


@app.route("/logout")
def logout():

    redis_store.delete(session.get('username'))
    session.pop('username')
    return redirect('/')


def is_logged(request):

    username = session.get('username')
    if username and redis_store.get(username):
        return True
    return False


def is_admin(request):

    username = session.get('username')
    user = ctr.is_admin(username)

    if user is None:
        return False
    return True
