from flask import Blueprint,render_template,request,flash,redirect

auth=Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form['email']
        firstName=request.form['firstName']
        password1=request.form['password1']
        password2=request.form['password2']

        if len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName)<2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1)<7:
            flash('Passwords must be atleast 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
        return redirect(request.url)   # PRG(Post-Redirect-Get)- without redirect, other flash messages will not flash out properly


    return render_template("sign_up.html")