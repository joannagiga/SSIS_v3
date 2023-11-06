from flask_mysql_connector import MySQL

mysql = MySQL()

def course_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM course"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses

def course_create(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO course (course_code, course_name, college_code) VALUES (%s, %s, %s)", (course_code, course_name, college_code))
    mysql.connection.commit()
    cursor.close()
    
def find_course(course_search, filter):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + course_search + "%"
    
    if filter == 'all':
        query = """
            SELECT * FROM course
            WHERE course_code LIKE %s
            OR course_name LIKE %s
            OR college_code LIKE %s
            """
        cursor.execute(query, (search_query, search_query, search_query))
    else:
        query = f"""
            SELECT * FROM course
            WHERE {filter} LIKE %s
        """
        cursor.execute(query, (search_query,))
    
    courses = cursor.fetchall()
    cursor.close()
    return courses



def delete_course(course_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM course WHERE course_code = %s", (course_code,))
    mysql.connection.commit()
    cursor.close()

def update_course(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE course SET course_name = %s, college_code= %s WHERE course_code =%s"
    cursor.execute(update_query, (course_name, college_code, course_code))
    mysql.connection.commit()
    cursor.close()

def get_collegeCode():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT college_code FROM college"
    cursor.execute(query)
    college_code = cursor.fetchall()
    cursor.close()
    return college_code

def check_courseCode(course_code):
    cursor = mysql.connection.cursor()
    query = "SELECT course_code FROM course where course_code = %s"
    cursor.execute(query, (course_code,))
    result = cursor.fetchone()
    cursor.close()
    return result