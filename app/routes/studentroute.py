from flask import *
from app.models.student import *
from flask_wtf import *
from config import CLOUDINARY_FOLDER
import re
import cloudinary
from cloudinary.uploader import upload as cloudinary_upload
from cloudinary.utils import cloudinary_url

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
        image_url = request.form['image_url']
        if not re.match(r'^\d{4}-\d{4}$', student_ID):
            flash('Invalid Student ID format. Follow YYYY-NNNN format.', 'error')
        elif check_student_ID(student_ID):
            flash('ID already exists!', 'error')
        else:
            student_create(student_ID, first_name, last_name, gender, course_code, year_level, image_url)
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
            students = find_students(search_query, 'all')
    return render_template('students.html', students=students)


@student_bp.route('/student/delete/<string:stud_ID>', methods=['DELETE'])
def remove_student(stud_ID):
    if request.method == 'DELETE':
        delete_student(stud_ID)
        flash('Student deleted successfully!', 'success')
        return jsonify({'success': True})


@student_bp.route('/student/edit/<string:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        gender = request.form.get('gender').capitalize()
        course_code = request.form.get('course_code').upper()
        year_level = request.form.get('year_level')
        image_url = request.form.get('image_url')
        update_student(student_id, first_name, last_name, gender, course_code, year_level, image_url)
        flash('Student edited successfully!', 'success')
        return redirect('/student/') 
    student_info = get_student_info(id)
    first_name = student_info['first_name']
    last_name = student_info['last_name']
    gender = student_info['gender']
    course_code = student_info['course_code']
    year_level = student_info['year_level']
    image_url = student_info['image_url']
    courses = get_courseCode()
    return render_template('editstudent.html', student_id=id, first_name=first_name, last_name=last_name, gender=gender, course_code=course_code, year_level=year_level, courses=courses, image_url=image_url)


@student_bp.route('/upload/cloudinary/', methods=['POST'])
def upload_to_cloudinary():
    file = request.files.get('file')

    if file:
        upload_result = cloudinary_upload(
            file, folder=CLOUDINARY_FOLDER)

        return jsonify({
            'is_success': True,
            'url': upload_result['secure_url']
        })

    return jsonify({
        'is_success': False,
        'error': 'Missing file'
    })
