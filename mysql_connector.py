def add_data(q,id,feedback):
    import pymysql.cursors
    connection = pymysql.connect(host="sql11.freemysqlhosting.net", user="sql11672622", password="KeeSghpbQI",database="sql11672622",cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "insert into Data(q, artwork_id, result) values(%s, %s, %s)"
            cursor.execute(sql, (q, id,feedback))
        connection.commit()