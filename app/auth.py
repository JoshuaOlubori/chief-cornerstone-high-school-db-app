from flask import render_template, redirect, request, url_for, flash, Blueprint, session
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, User
from werkzeug.security import generate_password_hash
from .forms import LoginForm, RegistrationForm, PasswordResetRequestForm, PasswordResetForm
auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('views.home')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)
        

@auth.route('/logout')
@login_required
def logout():
    #logout_user()
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now log in')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


# this function is called when 

# @auth.route('/reset', methods=['GET', 'POST'])
# def password_reset_request():
#     if not current_user.is_anonymous:
#         return redirect(url_for('main.index'))
#     form = PasswordResetRequestForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             return redirect(url_for('auth.password_reset'))
#     return render_template('auth/login.html')

@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            return redirect(url_for('auth.password_reset', user_id=user.id))
        else:
            flash('User not found.', 'danger')
            return(redirect(url_for('auth.login')))
    return render_template('auth/reset_password.html', form =form)


# @auth.route('/reset/<int:user_id>', methods=['GET', 'POST'])
# def password_reset():
#     if not current_user.is_anonymous:
#          return redirect(url_for('main.index'))
#     form = PasswordResetForm()
#     if form.validate_on_submit():
#         if User.reset_password(form.password.data):
#             db.session.commit()
#             flash('Your password has been updated.')
#             return redirect(url_for('auth.login'))
#         else:
#             return redirect(url_for('main.index'))
#     return render_template('auth/reset_password.html', form=form)

@auth.route('/reset/<int:user_id>', methods=['GET', 'POST'])
def password_reset(user_id):
    user = User.query.get(user_id)
    if not user:
         flash('User not found.', 'danger')
         return redirect(url_for('auth.login'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        current_user.password = form.password.data
        db.session.add(current_user)
        db.session.commit()
        flash('Password reset successful.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)