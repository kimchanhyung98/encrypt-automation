import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD'),
    db=os.environ.get('DB_DATABASE'),
    charset='utf8',
)
cursor = connection.cursor()


def count_column():  # return int
    sql = 'select count(*) from %s'
    table = os.environ.get('DB_TABLE')
    cursor.execute(sql, table)

    return cursor.fetchone()[0]
