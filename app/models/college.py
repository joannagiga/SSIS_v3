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

def delete_college(college_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM college WHERE college_code = %s", (college_code,))
    mysql.connection.commit()
    cursor.close()

def update_college(college_code, college_name):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE college SET college_name = %s WHERE college_code =%s"
    cursor.execute(update_query, (college_name, college_code))
    mysql.connection.commit()
    cursor.close()
    
def check_collegeCode(college_code):
    cursor = mysql.connection.cursor()
    query = "SELECT college_code FROM college where college_code = %s"
    cursor.execute(query, (college_code,))
    result = cursor.fetchone()
    cursor.close()
    return result
    


    
