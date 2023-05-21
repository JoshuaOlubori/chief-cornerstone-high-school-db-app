from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import StudentAdmissionForm, HODRegistrationForm, StaffRegistrationForm, TeacherRegistrationForm
from . import mysql_conn

bp = Blueprint('views', __name__)


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return redirect(url_for('auth.login'))

@bp.route('/cchs', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('index.html')

@bp.route('/cchs/student_registration', methods=['GET', 'POST'])
@login_required
def register_student():
    form = StudentAdmissionForm()
    if request.method == "POST" and form.validate_on_submit():
        first_name = form.first_name.data.title()
        last_name = form.last_name.data.title()
        dob = form.dob.data
        blood_group = form.blood_group.data.upper()
        genotype = form.genotype.data.upper()
        religion = form.religion.data
        address = form.address.data
        phone = form.phone.data
        ethnicity = form.ethnicity.data.title()
        city_town = form.city_town.data.title()
        medical = form.medical.data
        class_id = int(form.class_id.data)

        if medical.strip(" ") == "":
            medical = None 

        # save to MySQL database
        # check database connection
        try:
            cur = mysql_conn.connection.cursor()
        except:
            flash("Unable to connect to database. Check database credentials in __init__.py")

        # check calling the stored procedure 
        try:
            cur.callproc('register_student', 
                  [first_name, last_name, dob, blood_group, genotype, religion, address,
                    phone, ethnicity, city_town, medical, class_id])
            mysql_conn.connection.commit()
            cur.close()
            flash('Sucessfully registered')
        except:
            flash("Error in calling procedure")

        return redirect(url_for('views.register_student'))

    return render_template('registrationform.html', form=form)


@bp.route('/cchs/HOD_registration', methods=['GET', 'POST'])
@login_required
def register_hod():
    form = HODRegistrationForm() 
    if request.method == "POST" and form.validate_on_submit():
        id = int(form.id.data)
        first_name = form.first_name.data.title()
        last_name = form.last_name.data.title()
        dob = form.dob.data
        blood_group = form.blood_group.data.upper()
        genotype = form.genotype.data.upper()
        religion = form.religion.data
        address = form.address.data
        phone = form.phone.data
        s_phone = form.s_phone.data
        ethnicity = form.ethnicity.data.title()
        city_town = form.city_town.data.title()
        medical = form.medical.data
        bonus = form.bonus.data
        dept_id = int(form.dept_id.data)

        if medical.strip(" ") == "":
            medical = None 

        if s_phone.strip(" ") == "":
            s_phone = None

        if bonus.strip(" ") == "":
            bonus = None

         # save to MySQL database
         # check database connection
        try:
            cur = mysql_conn.connection.cursor()
        except:
            flash("Unable to connect to database. Check database credentials in __init__.py")

        # check calling the stored procedure
        try:
            cur.callproc('register_hod', 
                  [id, first_name, last_name, dob, blood_group, genotype, religion, address,
                    phone, s_phone, ethnicity, city_town, medical, bonus, dept_id])
            mysql_conn.connection.commit()
            cur.close()
            flash('Sucessfully registered')
        except:
            flash("Error in calling procedure")


        return redirect(url_for('views.register_hod'))

    return render_template('registrationform.html', form=form)


@bp.route('/cchs/staff_registration', methods=['GET', 'POST'])
@login_required
def register_staff():
    form = StaffRegistrationForm() 
    if request.method == "POST" and form.validate_on_submit():
        id = int(form.id.data)
        first_name = form.first_name.data.title()
        last_name = form.last_name.data.title()
        dob = form.dob.data
        blood_group = form.blood_group.data.upper()
        genotype = form.genotype.data.upper()
        religion = form.religion.data
        address = form.address.data
        phone = form.phone.data
        s_phone = form.s_phone.data
        ethnicity = form.ethnicity.data.title()
        city_town = form.city_town.data.title()
        medical = form.medical.data
        bonus = form.bonus.data
        dept_id = form.dept_id.data 

        # Inserting nulls into the database for blank attributes instead of whitespace for easier querying
        if medical.strip(" ") == "":
            medical = None 

        if s_phone.strip(" ") == "":
            s_phone = None

        if bonus.strip(" ") == "":
            bonus = None

         # save to MySQL database
         # check database connection
        try:
            cur = mysql_conn.connection.cursor()
        except:
            flash("Unable to connect to database. Check database credentials in __init__.py")

        # check calling the stored procedure
        try:
            cur.callproc('register_staff', 
                  [id, first_name, last_name, dob, blood_group, genotype, religion, address,
                    phone, s_phone, ethnicity, city_town, medical, bonus, dept_id])
            mysql_conn.connection.commit()
            cur.close()
            flash('Sucessfully registered')
        except:
            flash("Error in calling procedure")


        return redirect(url_for('views.register_staff'))

    return render_template('registrationform.html', form=form)


@bp.route('/cchs/teaching_staff_registration', methods=['GET', 'POST'])
@login_required
def register_teacher():
    form = TeacherRegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        id = int(form.id.data)
        first_name = form.first_name.data.title()
        last_name = form.last_name.data.title()
        dob = form.dob.data
        blood_group = form.blood_group.data.upper()
        genotype = form.genotype.data.upper()
        religion = form.religion.data
        address = form.address.data
        phone = form.phone.data
        s_phone = form.s_phone.data
        ethnicity = form.ethnicity.data.title()
        city_town = form.city_town.data.title()
        medical = form.medical.data
        bonus = form.bonus.data
        dept_id = form.dept_id.data 

        # Inserting nulls into the database for blank attributes instead of whitespace for easier querying
        if medical.strip(" ") == "":
            medical = None 

        if s_phone.strip(" ") == "":
            s_phone = None

        if bonus.strip(" ") == "":
            bonus = None

         # save to MySQL database
         # check database connection
        try:
            cur = mysql_conn.connection.cursor()
        except:
            flash("Unable to connect to database. Check database credentials in __init__.py")

        # check calling the stored procedure
        try:
            cur.callproc('register_teacher', 
                  [id, first_name, last_name, dob, blood_group, genotype, religion, address,
                    phone, s_phone, ethnicity, city_town, medical, bonus, dept_id])
            mysql_conn.connection.commit()
            cur.close()
            flash('Sucessfully registered')
        except:
            flash("Error in calling procedure")


        return redirect(url_for('views.register_teacher'))

    return render_template('registrationform.html', form=form)


@bp.route('/cchs/search', methods=['GET', 'POST'])
@login_required
def search():
    cur = mysql_conn.connection.cursor()
    if request.method == "POST":
        search_query = request.form["search_query"]

        # if search_query == " ":
        #     query = """
        #     SELECT * FROM person;
        #     """
        #     cur.execute(query)
        #     persons = cur.fetchall()
        #     cur.close()

            #query = "SELECT * FROM person WHERE person_id LIKE "%{}%" OR first_name LIKE "%{}%" OR last_name LIKE "%{}%" OR phone LIKE "%{}%";",('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%')
        
        query = "SELECT * FROM person WHERE person_id LIKE '%{}%' OR first_name LIKE '%{}%' OR last_name LIKE '%{}%' OR phone LIKE '%{}%'".format(search_query, search_query, search_query, search_query)
        cur.execute(query)
        persons = cur.fetchall()
        #print(persons)
        cur.close()

        return render_template('search.html', persons=persons)
    return render_template('search.html')






    
