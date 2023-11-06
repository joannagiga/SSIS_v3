from flask import *
from app.models.course import *
from flask_wtf import *

course_bp = Blueprint('course', __name__)

@course_bp.route('/course/')
def course():
    courses = course_list()
    
    return render_template('course.html', courses=courses )

@course_bp.route('/course/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college_code = request.form['college_code'].upper()
        if check_courseCode(course_code):
            flash('Course code already exists!', 'error')
        else:
            course_create(course_code, course_name, college_code)
            flash('Course added successfully!', 'success')
        return redirect('/course') 
    colleges = get_collegeCode()
    return render_template('addcourse.html', colleges=colleges)



@course_bp.route('/course/search', methods=['GET', 'POST'])
def search_course():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('course_search')
        filter = request.form.get('filter')
        if filter and search_query:
            courses = find_course(search_query, filter)
        elif not filter and search_query:
            # If no filter is selected, search across all fields
            courses = find_course(search_query, 'all')
    return render_template('course.html', courses=courses)




@course_bp.route('/course/delete/<string:course_code>', methods=['DELETE'])
def remove_course(course_code):
    if request.method == 'DELETE':
        delete_course(course_code)
        flash('Course deleted successfully!', 'success')
        return jsonify({'success': True})

@course_bp.route('/course/edit', methods=['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        course_name = request.form.get('course_name')
        college_code = request.form.get('college_code').upper()
        update_course(course_code, course_name, college_code)
        flash('Course edited successfully!', 'success')
        return redirect('/course/') 
    course_code = request.args.get('course_code')
    course_name = request.args.get('course_name')
    college_code = request.args.get('college_code')
    colleges = get_collegeCode()
    return render_template('editcourse.html', course_code=course_code, course_name=course_name, college_code=college_code, colleges=colleges)




