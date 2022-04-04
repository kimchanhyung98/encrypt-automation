import urllib.request
from urllib.parse import quote
from connect import *


# @param null
# @return int
def count_column():
    sql = 'select count(*) from %s'
    cursor.execute(sql, db_table)

    return cursor.fetchone()[0]


# @param int $user_id
# @return string $encrypted_data
def get_data(user_id):
    sql = 'select %s from %s where id = %s'
    cursor.execute(sql, (db_column, db_table, user_id))

    return cursor.fetchone()[0]


# @param string $encrypted_data
# @return string
def decrypt_data(encrypted_data):
    request = urllib.request.urlopen(api_url + quote(encrypted_data)).read()

    return request.decode('cp949')


# @param string $decrypted_data
# @param int $user_id
# @return null
def update_data(decrypted_data, user_id):
    sql = 'update %s set %s = %s where id = %s'
    cursor.execute(sql, (db_table, db_column, decrypted_data, user_id))
    # print('Updated')
    connection.commit()
