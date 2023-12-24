import pymysql.cursors

connection = pymysql.connect(host="sql11.freemysqlhosting.net", user="sql11672622", password="KeeSghpbQI",database="sql11672622",cursorclass=pymysql.cursors.DictCursor)
def conection_restart():
    global connection
    connection.close()
    connection = pymysql.connect(host="sql11.freemysqlhosting.net", user="sql11672622", password="KeeSghpbQI",database="sql11672622", cursorclass=pymysql.cursors.DictCursor)
def add_data(q,id,feedback):
    global connection
    while True:
        try:
            with connection:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "insert into Data(q, artwork_id, result) values(%s, %s, %s)"
                    cursor.execute(sql, (q, id,feedback))
                connection.commit()
            break
        except Exception as e:
            pass
def get_data(q,id):
    global connection
    while True:
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `q`, `artwork_id` FROM `Data` WHERE `q`=%s and `artwork_id`=%s"
                cursor.execute(sql, (q,id))
                result = cursor.fetchone()
                print(result)
                print(len(result))
            return result
        except Exception as e:
            pass

