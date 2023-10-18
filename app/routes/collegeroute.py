from flask import *
from app.models.college import *
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/college/')
def colleges():
    colleges = college_list()
    return render_template('college.html', colleges=colleges)

@college_bp.route('/college/', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        college_code = request.form['college_code']
        college_name = request.form['college_name']
        college_create(college_code, college_name)
        return redirect('/college') 
    return render_template('college.html')

