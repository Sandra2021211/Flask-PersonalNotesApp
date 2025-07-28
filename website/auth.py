from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email= request.form['email']
        password= request.form['password']

        user= User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')




    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form['email']
        first_name=request.form['firstName']
        password1=request.form['password1']
        password2=request.form['password2']

        user= User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name)<2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1)<7:
            flash('Passwords must be atleast 7 characters.', category='error')
        else:
            new_user=User(email=email, first_name=first_name, password= generate_password_hash(password1, method='pbkdf2:sha256')) #left params refers to models.py file and right params refers to the one in this file
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))


        return redirect(request.url)   # PRG(Post-Redirect-Get)- without redirect, other flash messages will not flash out properly


    return render_template("sign_up.html")