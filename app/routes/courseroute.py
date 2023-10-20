from flask import *
from app.models.course import *
from flask_wtf import *

course_bp = Blueprint('course', __name__)

@course_bp.route('/course/')
def course():
    courses = course_list()
    return render_template('course.html', courses=courses)

@course_bp.route('/course/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college_code = request.form['college_code']
        course_create(course_code, course_name, college_code)
        return redirect('/course') 
    return render_template('course.html')

@course_bp.route('/course/search', methods=['GET', 'POST'])
def search_course():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('course_search')
        if search_query:
            courses = find_course(search_query)
    return render_template('course.html', courses=courses)

@course_bp.route('/course/delete/<string:course_code>', methods=['DELETE'])
def remove_course(course_code):
    if request.method == 'DELETE':
        print(course_code)
        delete_course(course_code)
        return jsonify({'success': True})

@course_bp.route('/course/edit', methods=['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        college_code = request.form.get('college_code').upper()
        update_course(course_code, course_name, college_code)
        return redirect('/course/') 
    course_code = request.args.get('course_code')
    course_name = request.args.get('course_name')
    college_code = request.args.get('college_code')
    colleges = get_collegeCode()
    return render_template('editcourse.html', course_code=course_code, course_name=course_name, college_code=college_code, colleges=colleges)




