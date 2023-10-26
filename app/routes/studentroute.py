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
        student_ID = request.form['student_ID']
        first_name= request.form['first_name'].title()
        last_name = request.form['last_name'].title()
        gender = request.form['gender'].capitalize()
        course_code = request.form['course_code'].upper()
        year_level = request.form['year_level']
        if check_student_ID(student_ID):
            flash('ID already exists!', 'error')
        else:
            student_create(student_ID, first_name, last_name, gender, course_code, year_level)
            flash('Student added successfully!', 'success')
        return redirect('/student') 
    courses = get_courseCode()
    return render_template('addstudents.html', courses=courses)


@student_bp.route('/student/search', methods=['POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        filter = request.form.get('filter')
        if filter and search_query:
            students = find_students(search_query, filter)
        elif not filter and search_query:
            # If no filter is selected, search across all fields
            students = find_students(search_query, 'all')
    return render_template('students.html', students=students)


@student_bp.route('/student/delete/<string:stud_ID>', methods=['DELETE'])
def remove_student(stud_ID):
    if request.method == 'DELETE':
        delete_student(stud_ID)
        flash('Student deleted successfully!', 'success')
        return jsonify({'success': True})


@student_bp.route('/student/edit', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        gender = request.form.get('gender').capitalize()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        update_student(student_id, first_name, last_name, gender, course_code, year_level)
        flash('Student edited successfully!', 'success')
        return redirect('/student/') 
    student_id = request.args.get('student_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    gender = request.args.get('gender')
    course_code = request.args.get('course_code')
    year_level = request.args.get('year_level')
    courses = get_courseCode()
    return render_template('editstudent.html', student_id=student_id, first_name=first_name, last_name=last_name, gender=gender, course_code=course_code, year_level=year_level, courses=courses)



