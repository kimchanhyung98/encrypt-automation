import pymysql


connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    db='test',
    charset='utf8',
)
cursor = connection.cursor()
sql = 'select * from test'
cursor.execute(sql)
data = cursor.fetchall()
print(data)