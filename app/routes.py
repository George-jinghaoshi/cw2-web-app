from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm, ProductForm
from app.models import User, Product, Cart
from app import db

main = Blueprint('main', __name__)

@main.route("/")
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    
   
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        home()
    #form = LoginForm()
    #if form.validate_on_submit():
    #    user = User.query.filter_by(email=form.email.data).first()
     #   if user:  
    #        login_user(user)
     #       flash('You have been logged in!', 'success')
    ##        return redirect(url_for('main.home'))
    #    else:
     #       flash('Login Unsuccessful. Please check your email.', 'danger')
    #return render_template('login.html', form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))

@main.route("/cart")
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@main.route("/add_to_cart/<int:product_id>", methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart_item = Cart.query.filter_by(user_id='123', product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(user_id='123', product_id=product_id, quantity=1)
        db.session.add(cart_item)
    db.session.commit()
    flash(f'{product.name} added to your cart!', 'success')
    return redirect(url_for('main.cart'))

@main.route("/product/<int:product_id>")
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)
