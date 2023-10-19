from flask_mysql_connector import MySQL

mysql = MySQL()

def college_list():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT * FROM college"
    cursor.execute(query)
    colleges = cursor.fetchall()
    cursor.close()
    return colleges

def college_create(college_code, college_name):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO college (college_code, college_name) VALUES (%s, %s)", (college_code, college_name))
    mysql.connection.commit()
    cursor.close()
    
def find_college(college_search):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + college_search + "%"
    cursor.execute("SELECT * FROM college WHERE college_code LIKE %s OR college_name LIKE %s", (search_query, search_query ))
    colleges = cursor.fetchall()
    cursor.close()
    return colleges
    

    
