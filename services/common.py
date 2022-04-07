import urllib.request
from urllib.parse import quote
from services.connect import *


# @param null
# @return int
def count_column():
    sql = 'select count(*) from ' + db_table
    cursor.execute(sql)

    return int(cursor.fetchone()[0])


# @param int $user_id
# @return string $encrypted_data
def get_data(user_id):
    sql = 'select ' + db_column + ' from ' + db_table + ' where id = ' + str(user_id)
    cursor.execute(sql)

    return cursor.fetchone()[0]


# @param string $encrypted_data
# @return string
def decrypt_data(encrypted_data):
    decrypted_data = urllib.request.urlopen(api_url + quote(encrypted_data)).read()
    decode_data = decrypted_data.decode('cp949')

    return decode_data


# @param string $decrypted_data
# @param int $user_id
# @return null
def update_data(decrypted_data, user_id):
    sql = 'update ' + db_table + ' set ' + db_column + ' = "' + decrypted_data + '" where id = ' + str(user_id)
    cursor.execute(sql)
    connection.commit()
