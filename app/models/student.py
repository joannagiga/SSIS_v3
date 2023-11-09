from flask_mysql_connector import MySQL

mysql = MySQL()

def student_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = """
    SELECT student.*, CONCAT(college.college_name, ' (',course.college_code, ')') AS college_info
    FROM student
    JOIN course ON student.course_code = course.course_code
    JOIN college ON course.college_code = college.college_code
    """
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def student_create(ID, first_name, last_name, gender, course_code, year_level):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO student (ID, first_name, last_name, gender, course_code, year_level) VALUES (%s, %s, %s, %s, %s, %s)", (ID, first_name, last_name, gender, course_code, year_level))
    mysql.connection.commit()
    cursor.close()
    
    
def find_students(searchstudent, filter):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchstudent + "%"
    
    if filter == 'all':
        query = """
            SELECT student.*, CONCAT(course.college_code, ' (', college.college_name, ')') AS college_info
            FROM student
            JOIN course ON student.course_code = course.course_code
            JOIN college ON course.college_code = college.college_code
            WHERE ID LIKE %s
            OR first_name LIKE %s
            OR last_name LIKE %s
            OR (gender = %s)  -- Exact match for gender
            OR year_level LIKE %s
            OR course_code LIKE %s
            OR CONCAT(course.college_code, ' (', college.college_name, ')') LIKE %s  -- Search by college
            """
        cursor.execute(query, (search_query, search_query, search_query, searchstudent, search_query, search_query, search_query))
    else:
        if filter == 'gender':
            gender_search = searchstudent + "%"
            query = f"""
                SELECT student.*, CONCAT(course.college_code, ' (', college.college_name, ')') AS college_info
                FROM student
                JOIN course ON student.course_code = course.course_code
                JOIN college ON course.college_code = college.college_code
                WHERE {filter} = %s  -- Exact match for gender
            """
            cursor.execute(query, (gender_search,))
        elif filter == 'college_info':  # Handle the new filter for searching by college
            query = """
                SELECT student.*, CONCAT(course.college_code, ' (', college.college_name, ')') AS college_info
                FROM student
                JOIN course ON student.course_code = course.course_code
                JOIN college ON course.college_code = college.college_code
                WHERE CONCAT(course.college_code, ' (', college.college_name, ')') LIKE %s
            """
            cursor.execute(query, (search_query,))
        else:
            query = f"""
                SELECT student.*, CONCAT(course.college_code, ' (', college.college_name, ')') AS college_info
                FROM student
                JOIN course ON student.course_code = course.course_code
                JOIN college ON course.college_code = college.college_code
                WHERE {filter} LIKE %s
            """
            cursor.execute(query, (search_query,))
    
    students = cursor.fetchall()
    cursor.close()
    return students



def delete_student(stud_ID):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM student WHERE ID = %s", (stud_ID,))
    mysql.connection.commit()
    cursor.close()

def update_student(student_id, first_name, last_name, gender, course_code, year_level):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE student SET first_name = %s, last_name = %s, gender = %s, course_code = %s, year_level = %s WHERE ID = %s"
    cursor.execute(update_query, (first_name, last_name, gender, course_code, year_level, student_id))
    mysql.connection.commit()
    cursor.close()
    
def get_courseCode():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT course_code FROM course"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def check_student_ID(student_ID):
    cursor = mysql.connection.cursor()
    query = "SELECT ID FROM student where ID = %s"
    cursor.execute(query, (student_ID,))
    result = cursor.fetchone()
    cursor.close()
    return result