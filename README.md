# Decrypt Automation

마이그레이션 작업 중 암호화된 데이터 암호화&복호화 작업 자동화  
API는 [kimchanhyung98](https://github.com/kimchanhyung98) DM

이메일 검증 함수는 추가하였으나 사용하고 있지 않음

### .env

```dotenv
# api
API_DECRYPT_URL=
API_ENCRYPT_URL=

# crypt
CRYPT_TYPE=
# encrypt or decrypt

# db
DB_HOST=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=

DB_TABLE=
DB_COLUMN=

```

### Install Packages

```shell
pip install PyMySQL python-dotenv
```
