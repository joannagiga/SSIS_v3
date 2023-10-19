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
    
def find_course(course_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + course_search + "%"
    cursor.execute("SELECT * FROM course WHERE course_code LIKE %s OR course_name LIKE %s OR college_code LIKE %s", (search_query, search_query, search_query ))
    courses = cursor.fetchall()
    cursor.close()
    return courses

def delete_course(course_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM course WHERE course_code = %s", (course_code,))
    mysql.connection.commit()
    cursor.close()
    