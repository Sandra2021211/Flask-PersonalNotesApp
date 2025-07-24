from flask import Blueprint,render_template,request

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
            pass
        elif len(firstName)<2:
            pass
        elif password1 != password2:
            pass
        elif len(password1)<7:
            pass
        else:
            #add user to db
            pass


    return render_template("sign_up.html")