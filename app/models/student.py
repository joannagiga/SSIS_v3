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
    
    
def find_students(searchstudent):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchstudent + "%"
    cursor.execute("SELECT * FROM student WHERE ID LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR gender LIKE %s OR course_code LIKE %s OR year_level LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students