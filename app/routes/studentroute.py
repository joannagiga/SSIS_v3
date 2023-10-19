from flask import *
from app.models.student import *
from flask_wtf import *

student_bp = Blueprint('student', __name__)

@student_bp.route('/student/', methods=['GET', 'POST'])
def students():
    students = student_list()
    return render_template('students.html', students=students)

@student_bp.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_ID = request.form['ID']
        first_name= request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        course_code = request.form['course_code']
        year_level = request.form['year_level']
        student_create(student_ID, first_name, last_name, gender, course_code, year_level)
        return redirect('/student') 
    return render_template('students.html')


@student_bp.route('/student/search', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_students(search_query)
    return render_template('students.html', students=students)
