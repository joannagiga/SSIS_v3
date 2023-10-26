from flask import *
from app.models.college import *
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/college/')
def colleges():
    colleges = college_list()
    return render_template('college.html', colleges=colleges)

@college_bp.route('/college/add', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        college_code = request.form['college_code'].upper()
        college_name = request.form['college_name'].title()
        if check_collegeCode(college_code):
            flash('College code already exists!', 'error')
        else:
            college_create(college_code, college_name)
            flash('College added successfully!', 'success')
        return redirect('/college') 
    return render_template('addcollege.html')

@college_bp.route('/college/search', methods=['GET', 'POST'])
def search_college():
    colleges = []
    if request.method == 'POST':
        search_query = request.form.get('college_search')
        if search_query:
            colleges = find_college(search_query)
    return render_template('college.html', colleges=colleges)

@college_bp.route('/college/delete/<string:college_code>', methods=['DELETE'])
def remove_college(college_code):
    if request.method == 'DELETE':
        delete_college(college_code)
        flash('College deleted successfully!', 'success')
        return jsonify({'success': True})

@college_bp.route('/college/edit', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        college_code = request.form.get('college_code').upper()
        college_name = request.form.get('college_name')
        update_college(college_code, college_name)
        flash('College edited successfully!', 'success')
        return redirect('/college/') 
    college_code = request.args.get('college_code')
    college_name = request.args.get('college_name')

    return render_template('editcollege.html', college_code=college_code, college_name=college_name)







