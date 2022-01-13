import os
import pymysql
import urllib.request
from dotenv import load_dotenv
load_dotenv()


def get_email(user_id):
    connection = pymysql.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        db=os.environ.get('MYSQL_DB'),
        charset='utf8',
    )
    cursor = connection.cursor()
    sql = 'select user_email from member_email_encrypt where id = %s'
    cursor.execute(sql, user_id)
    return cursor.fetchone()[0]


def decrypt_email(email):
    url = os.environ.get('DECRYPT_API_URL')
    request = urllib.request.urlopen(url + email).read()
    return request.decode('utf-8').split()[0]


encrypted_email = get_email(187593)
decrypted_email = decrypt_email(encrypted_email)
print(decrypted_email)
