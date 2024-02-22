## requirements:
- docker
- docker compose

to run project simply use:  
```shell
docker compose up
```
adding superuser:
```shell
 docker exec schedule python manage.py createsuperuser --noinput \
 --username admin \
 --email admin@admin.pl
```
password is set in dpp.env file
- Files containng **enviromantal variables** and **secrets** are included for demonstration purposes
## usage

- server runs on **localhost:8000** by default
- endpoints documentation is available on **localhost:8000/docs/**
- in order to use secured endpoints user need to obtain token by **registering** or **logging in**
- - token needs to be placed in Authorization header like:
    ```http request
      Authorization Token <user_token>
    ```
- sample requests are exported from insomnia (insomnia v4 (JSON)) and are stored in sample.json file.
- - in order to use it:
- - 1. import file into insomnia
- - 2. register user (token is included in response)
- - 3. Paste toke into Authorization header (<user_token>)


