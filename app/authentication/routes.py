# Import necessary modules
from forms import UserLogInForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

# Create a blueprint for authenication
auth = Blueprint("auth", __name__, template_folder="auth_templates")

# Route for user sign-up
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLogInForm()

    try:
        # If form is submitted and validated, create a new user and redirect to homepage
        if request.method == 'POST' and form.validate_on_submit():
            # get email and data from the form data
            email = form.email.data
            password = form.password.data
            print(email, password)

            # create a new user and add to database
            user = User(email, password = password)

            # Add the new user to the database and commit the changes
            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'User-created')
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid Form data: Please check your Form')
    
    # render the signup.html template with the UserLogInForm instance
    return render_template('signup.html', form = form)

 # route for user sign in   
@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLogInForm()
    
    try:
        # If form is submitted and validated, sign in user and redirect to profile page
        if request.method == 'POST' and form.validate_on_submit():
            # Get email and password from data
            email = form.email.data
            password = form.password.data
            print(email,password)

            # Check if the email and password are correct
            logged_user = User.query.filter(User.email == email).first()
            # If a user with the provided email exists, check if the provided password is correct
            if logged_user and check_password_hash(logged_user.password, password):
                # If the password is correct, log in the user and flash a success message
                login_user(logged_user)
                flash('You have succesfully logged in!', 'auth-success')
                return redirect(url_for('site.profile'))
            else:
                # If the password is incorrect, flash an error message and redirect to the signin page
                flash('Please check your Email/Password.', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        # Raise an exception if the form data is invalid
        raise Exception('Invalid Form Data: Please Check your Form')
    # Render the signin template with the form object
    return render_template('signin.html', form=form)

# Route for user logout
@auth.route('/logout')
def logout():
    # Log out the current user and redirect to the homepage
    logout_user()
    return redirect(url_for('site.home'))