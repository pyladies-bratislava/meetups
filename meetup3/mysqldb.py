import pymysql

# Connect to the database
host, user, password, db = '192.168.223.182', 'pyladies', 'pyladies', 'employees'

connection = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT COUNT(*) FROM departments;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
