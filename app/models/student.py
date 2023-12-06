from flask_mysql_connector import MySQL

mysql = MySQL()

def student_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = """
    SELECT student.*, CONCAT(college.college_name, ' (',course.college_code, ')') AS college_info
    FROM student
    JOIN course ON student.course_code = course.course_code
    JOIN college ON course.college_code = college.college_code
    ORDER BY student.ID
    """
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def student_create(ID, first_name, last_name, gender, course_code, year_level, image_url):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO student (ID, first_name, last_name, gender, course_code, year_level, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (ID, first_name, last_name, gender, course_code, year_level, image_url))
    mysql.connection.commit()
    cursor.close()
    
    
def find_students(searchstudent, filter):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchstudent + "%"
    
    if filter == 'all':
        query = """
            SELECT s.*, CONCAT(c.course_code, ' (', cl.college_name, ')') AS college_info
            FROM student AS s
            JOIN course AS c ON s.course_code = c.course_code
            JOIN college AS cl ON c.college_code = cl.college_code
            WHERE s.ID LIKE %s
            OR s.first_name LIKE %s
            OR s.last_name LIKE %s
            OR s.gender = %s
            OR s.year_level LIKE %s
            OR s.course_code LIKE %s
            OR CONCAT(c.course_code, ' (', cl.college_name, ')') LIKE %s
            """
        cursor.execute(query, (search_query, search_query, search_query, searchstudent, search_query, search_query, search_query))
    else:
        if filter == 'gender':
            gender_search = searchstudent
            query = """
                SELECT s.*, CONCAT(c.course_code, ' (', cl.college_name, ')') AS college_info
                FROM student AS s
                JOIN course AS c ON s.course_code = c.course_code
                JOIN college AS cl ON c.college_code = cl.college_code
                WHERE s.gender = %s
            """
            cursor.execute(query, (gender_search,))
        elif filter == 'college_info':
            query = """
                SELECT s.*, CONCAT(c.course_code, ' (', cl.college_name, ')') AS college_info
                FROM student AS s
                JOIN course AS c ON s.course_code = c.course_code
                JOIN college AS cl ON c.college_code = cl.college_code
                WHERE CONCAT(c.course_code, ' (', cl.college_name, ')') LIKE %s
            """
            cursor.execute(query, (search_query,))
        else:
            # Use the table alias for course_code in the WHERE clause
            query = f"""
                SELECT s.*, CONCAT(c.course_code, ' (', cl.college_name, ')') AS college_info
                FROM student AS s
                JOIN course AS c ON s.course_code = c.course_code
                JOIN college AS cl ON c.college_code = cl.college_code
                WHERE s.{filter} LIKE %s
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

def update_student(student_id, first_name, last_name, gender, course_code, year_level, image_url):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE student SET first_name = %s, last_name = %s, gender = %s, course_code = %s, year_level = %s,  image_url = %s WHERE ID = %s"
    cursor.execute(update_query, (first_name, last_name, gender, course_code, year_level, image_url, student_id))
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

def get_student_info(student_ID):
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM student where ID = %s"
    cursor.execute(query, (student_ID,))
    result = cursor.fetchone()
    cursor.close()
    return result

