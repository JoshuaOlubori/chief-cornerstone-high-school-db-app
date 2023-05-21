from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, SelectField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Optional
from .models import User
from wtforms import ValidationError


# AUTHENTICATION
# form for logging in users
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
    

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
        

class PasswordResetRequestForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')




# MAIN FORMS
class StudentAdmissionForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 45, message="Incorrect length")])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 45, message="Incorrect length")])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    blood_group = StringField('Blood group', validators=[DataRequired(), Length(1,4, message="Incorrect length")])
    genotype = StringField('Genotype', validators=[DataRequired(), Length(1,2, message="Incorrect length") ])
    religion = SelectField('Religion', choices=['Christianity', 'Islam', 'Others'], validators=[DataRequired()])
    address = TextAreaField('Address')
    phone = StringField('Phone Number', validators=[DataRequired(), Length(11, 11, message="Incorrect length") ])
    ethnicity = StringField('Ethnicity', validators=[DataRequired(), Length(1, 45, message="Incorrect length")])
    city_town = StringField('City or town of residence', validators=[DataRequired(), Length(1, 45, message="Incorrect length")])
    medical = StringField('Medical Condition(s)', validators=[Optional()])
    class_id = StringField('Class ID')

class HODRegistrationForm(FlaskForm):
    id = StringField('ID Number (Insert zero (0) if individual does not exist in the database)',  validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 45)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 45)])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    blood_group = StringField('Blood group', validators=[DataRequired(), Length(1,4)])
    genotype = StringField('Genotype', validators=[DataRequired(), Length(1,2) ])
    religion = SelectField('Religion', choices=['Christianity', 'Islam', 'Others'], validators=[DataRequired()])
    address = TextAreaField('Address')
    phone = StringField('Phone Number', validators=[DataRequired(), Length(11, 11) ])
    s_phone = StringField('Spouse Phone Number (Leave blank if individual is unmarried)', validators=[Length(11, 11), Optional()])
    ethnicity = StringField('Ethnicity', validators=[DataRequired(), Length(1, 45)])
    city_town = StringField('City or town of residence', validators=[DataRequired(), Length(1, 45)])
    medical = StringField('Medical Condition(s) (Leave blank if none)', validators=[Length(1, 45), Optional()])
    bonus = StringField('Bonus (Leave blank if none)', validators=[Optional()])
    dept_id = StringField(' Department ID Number', validators=[DataRequired()])

class StaffRegistrationForm(FlaskForm):
    id = StringField('ID Number (Insert zero (0) if individual does not exist in the database)',  validators=[DataRequired(), Length(1, 45)])
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 45)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 45)])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    blood_group = StringField('Blood group', validators=[DataRequired(), Length(1,4)])
    genotype = StringField('Genotype', validators=[DataRequired(),Length(1,2) ])
    religion = SelectField('Religion', choices=['Christianity', 'Islam', 'Others'], validators=[DataRequired()])
    address = TextAreaField('Address')
    phone = StringField('Phone Number (Enter an 11-digit phone number e.g(080********))', validators=[DataRequired(), Length(11, 11) ])
    s_phone = StringField('Spouse Phone Number', validators=[Length(11, 11), Optional()])
    ethnicity = StringField('Ethnicity', validators=[DataRequired(), Length(1, 45)])
    city_town = StringField('City or town of residence', validators=[DataRequired(), Length(1, 45)])
    medical = StringField('Medical Condition(s)', validators=[Length(1, 45), Optional()])
    bonus = StringField('Bonus')
    dept_id = StringField('Department ID', validators=[DataRequired()])

class TeacherRegistrationForm(FlaskForm):
    id = StringField('ID Number (Insert zero (0) if individual does not exist in the database)',  validators=[DataRequired(), Length(1, 45)])
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 45)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 45)])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    blood_group = StringField('Blood group', validators=[DataRequired(), Length(1,4)])
    genotype = StringField('Genotype', validators=[DataRequired(),Length(1,2) ])
    religion = SelectField('Religion', choices=['Christianity', 'Islam', 'Others'], validators=[DataRequired()])
    address = TextAreaField('Address')
    phone = StringField('Phone Number (Enter an 11-digit phone number e.g(080********))', validators=[DataRequired(), Length(11, 11) ])
    s_phone = StringField('Spouse Phone Number', validators=[Length(11, 11), Optional()])
    ethnicity = StringField('Ethnicity', validators=[DataRequired(), Length(1, 45)])
    city_town = StringField('City or town of residence', validators=[DataRequired(), Length(1, 45)])
    medical = StringField('Medical Condition(s)', validators=[Length(1, 45), Optional()])
    bonus = StringField('Bonus')
    dept_id = StringField('Department ID', validators=[DataRequired()])

class SearchForm(FlaskForm):
    id = StringField('ID Number (Insert zero (0) if individual does not exist in the database)',  validators=[Length(1, 45)])
    first_name = StringField('First name', validators=[Length(1, 45)])
    last_name = StringField('Last name', validators=[Length(1, 45)]) 
    phone = StringField('Phone Number (Enter an 11-digit phone number e.g(080********))', validators=[Length(11, 11) ])