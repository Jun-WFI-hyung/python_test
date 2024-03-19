import pymysql

db_ip = 'localhost'
db_port = 3306
db_id = 'root'
db_pw = 'dsa804c'
db_name = 'adwsdb'
db = pymysql.connect(host=db_ip, port=db_port, user=db_id, passwd=db_pw, db=db_name, charset='utf8')

with db.cursor() as cursor:
    sql = '''
        SELECT * FROM user
    '''
    try:
        ret = cursor.execute(sql)
        db.commit()
    except Exception as E:
        pass
    else:
        for i in cursor:
            print(i)
    finally:
        db.close()