# loans_macropay

#### Dependencias
- Docker
- Python 3.11
- Django 5.0.4

#### En la ráiz del proyecto, crear un archivo un .env y agregar lo siguiente:
```
    MYSQL_ROOT_PASSWORD=root_pass_mysql
    MYSQL_DATABASE=loans
    MYSQL_USER=user_mysql
    MYSQL_PASSWORD=pass_mysql
   ```

#### Compilar el proyecto:
- ```docker-compose build```

#### Correr las migraciones (poblar tablas):
- ```docker-compose run web python manage.py migrate```


#### Crear usuario admin (nos servirá para entrar al panel administrativo y documentación api)
- ```docker-compose run web python manage.py createsuperuser```

#### Levantar el proyecto:
- ```docker-compose up```


#### Documentación api
- ```http://localhost:8000/api/doc/```

#### Panel administrativo
- ```http://localhost:8000/admin/```

#### Ejecutar los tests
- ```docker-compose run web python manage.py test```