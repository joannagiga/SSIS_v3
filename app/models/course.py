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