# SETUP TO RUN PROJECTS
```angular2
make sure you have already below list in your system:
python 3.7
postgresSQL (database)
```

```angular2
Create virtualenv and activate virtualenv
Install all packages from requirements.txt file
pip install -r requirements.txt
setup database: ​ 
a)  ​- create user with password ​ 
    - create database with above user ​
    - grant all permission to it. ​	​ 

create user <user_name> with password '<password>'; 
​create database <db_name> with owner <user_name>; ​	
grant all privileges on database <db_name> to <user_name>; ​	​

​b) ​- create local.py file from settings 
​	​inside krazybee folder settings i.e krazybee/settings 
​	​- add database in local.py ​	​	
import os 
DEBUG = True ​ 
DATABASES = { ​ 'default': { ​ 'ENGINE': 'django.db.backends.postgresql_psycopg2', ​ 'NAME': os.environ.get('DB_NAME', ''), ​ 'HOST': os.environ.get('DB_HOST', ''), ​ 'USER': os.environ.get('DB_USER', ''), ​ 'PASSWORD': os.environ.get('DB_PASSWORD', ''), ​ 'PORT': os.environ.get('DB_PORT', '5432') ​ } ​ } ​

```

run migrate
./manage.py migrate
create token for API: ​ - create super user from terminal ​ - login from admin ​ - create token
run project
./manage.py runserver
API for GET fetch data :
​    - endpoint: '/fetch/data/' 
    - params: {
        type: '',
        album: '',
        id: ''
    }
​     - header: {
​                "Authorization": "Token <created_token>"
​              }

API for GET insert data:
​    - endpoint: '/insert/data/' 
​    - header: {
​                "Authorization": "Token <created_token>"
​              }
​          