import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

api_url = os.environ.get('API_URL')
db_table = os.environ.get('DB_TABLE')
db_column = os.environ.get('DB_COLUMN')

connection = pymysql.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD'),
    db=os.environ.get('DB_DATABASE'),
    charset='utf8',
)
cursor = connection.cursor()
