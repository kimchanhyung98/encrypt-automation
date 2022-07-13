import urllib.request
from urllib.parse import quote
from services.connect import *


# @param  null
# @return  int
def count_column():
    sql = 'select count(*) from ' + db_table
    cursor.execute(sql)

    return int(cursor.fetchone()[0])


# @param  int user_id
# @return  string
def get_data(user_id):
    sql = 'select ' + db_column + ' from ' + db_table + ' where id = ' + str(user_id)
    cursor.execute(sql)

    return cursor.fetchone()[0]


# @param  int count
# @param  string encrypted_data
# @return  string
def crypto(count, data):
    try:
        processed_data = crypto_process(data, 'cp949')
    except UnicodeDecodeError as e:
        print(e)
        print('id: ', count, ', error: ', data)

        try:
            processed_data = crypto_process(data, 'utf-8')
        except:
            processed_data = data

    return processed_data


# @param  string data
# @param  string encoding_type
# @return  string
def crypto_process(data, encoding_type):
    # encrypt
    if crypt_type == 'encrypt':
        encrypted_data = urllib.request.urlopen(api_encrypt_url + quote(data)).read()
        processed_data = encrypted_data.decode(encoding_type)
        # print('encrypted: ', processed_data)
    # decrypt
    else:
        if len(data) > 20:
            decrypted_data = urllib.request.urlopen(api_decrypt_url + quote(data)).read()
            processed_data = decrypted_data.decode(encoding_type)
            # print('decrypted: ', processed_data)
        else:
            processed_data = data
            # print('not_decrypted: ', processed_data)

    return processed_data


# @param  string processed_data
# @param  int user_id
# @return  null
def update_data(processed_data, user_id):
    sql = 'update ' + db_table + ' set ' + db_column + ' = "' + processed_data + '" where id = ' + str(user_id)
    cursor.execute(sql)
    connection.commit()
