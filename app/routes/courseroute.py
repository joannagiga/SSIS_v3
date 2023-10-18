from flask import *
from app.models.course import *
from flask_wtf import *

course_bp = Blueprint('course', __name__)

@course_bp.route('/course/')
def course():
    courses = course_list()
    return render_template('course.html', courses=courses)

@course_bp.route('/course/', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        college_code = request.form['college_code']
        course_create(course_code, course_name, college_code)
        return redirect('/course') 
    return render_template('course.html')
