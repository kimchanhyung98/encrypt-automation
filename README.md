# Decrypt Automation

마이그레이션 작업 중 암호화&복호화된 데이터, 처리 작업 자동화  
API는 [kimchanhyung98](https://github.com/kimchanhyung98) DM

이메일 검증 함수는 추가하였으나 사용하고 있지 않음(`services/email.py`)


### .env
```dotenv
# api
API_DECRYPT_URL=https://decrypt.domain
API_ENCRYPT_URL=https://encrypt.domain

# crypt
CRYPT_TYPE=true

# db
DB_HOST=127.0.0.1
DB_DATABASE=database
DB_USERNAME=admin
DB_PASSWORD=password

DB_TABLE=table
DB_COLUMN=column
```


### Install Packages
```shell
pip install PyMySQL python-dotenv
```
