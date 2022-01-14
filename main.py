import os
import re
import pymysql
import urllib.request
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def get_email(user_id):
    sql = 'select user_email from member_email_encrypt where id = %s'
    cursor.execute(sql, user_id)
    return cursor.fetchone()[0]


def decrypt_email(email):
    url = os.environ.get('DECRYPT_API_URL')
    request = urllib.request.urlopen(url + quote(email)).read()
    return request.decode('cp949')


def update_email(email, user_id):
    sql = 'update member_email_encrypt set user_email = %s where id = %s'
    cursor.execute(sql, (email, user_id))
    connection.commit()


def check_email(email):
    if not re.fullmatch(regex, email):
        print(email)


connection = pymysql.connect(
    host=os.environ.get('MYSQL_HOST'),
    user=os.environ.get('MYSQL_USER'),
    password=os.environ.get('MYSQL_PASSWORD'),
    db=os.environ.get('MYSQL_DB'),
    charset='utf8',
)
cursor = connection.cursor()

i = 1
while i < 999:
    encrypted_email = get_email(i)
    # print('id: ', i, ', encrypt: ', encrypted_email)
    decrypted_email = decrypt_email(encrypted_email)
    # print('id: ', i, ', decrypt: ', decrypted_email)
    check_email(decrypted_email)
    update_email(decrypted_email, i)
    i = i + 1
