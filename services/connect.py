import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

# api
api_decrypt_url = os.environ.get('API_DECRYPT_URL')
api_encrypt_url = os.environ.get('API_ENCRYPT_URL')
# crypt
crypt_type = os.environ.get('CRYPT_TYPE')
# db
db_table = os.environ.get('DB_TABLE')
db_column = os.environ.get('DB_COLUMN')

# mysql connect
connection = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD'),
    db=os.environ.get('DB_DATABASE'),
    charset='utf8',
)
cursor = connection.cursor()
