from mobao import app
from flask import render_template, request, g, redirect, url_for, session
from mobao.models import product, user


@app.route('/')
@app.route('/list')
def list_product():
    return render_template('list.html', products=product.get_product_all())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        login_name = request.form['name']
        login_password = request.form['password']
        login_user = user.authenticate_user(login_name, login_password)
        if login_user:
            session['user'] = login_user
            return redirect(url_for('list_product'))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('list_product'))


@app.route('/checkout', methods=['POST'])
def check_out():
    if request.method == 'POST':
        if 'user' in session:
            return render_template('checkout_complete.html')
        else:
            return redirect(url_for('login'))
    else:
        pass

