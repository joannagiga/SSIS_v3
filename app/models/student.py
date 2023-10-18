from flask_mysql_connector import MySQL

mysql = MySQL()

def student_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM student"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def student_create(ID, first_name, last_name, gender, course_code, year_level):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO student (ID, first_name, last_name, gender, course_code, year_level) VALUES (%s, %s, %s, %s, %s, %s)", (ID, first_name, last_name, gender, course_code, year_level))
    mysql.connection.commit()
    cursor.close()