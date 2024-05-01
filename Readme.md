## Django App
The implementation of a powerful API using Django Rest Framework.
With data storage seamlessly integrated into a database, we've optimized
retrieval efficiency by incorporating pagination for streamlined information access.

Our project boasts a comprehensive CRUD functionality tailored specifically for
managing cart items.

## Running app
Use the next command:
```bash
pip install -r requirements.txt
cd shopping_cart
python manage.py migrate
python manage.py runserver
```
## Initial steps
```bash
pip install django
pip install djangorestframework
django-admin startproject shopping_cart
cd shopping_cart
python manage.py startapp api
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

```bash
python manage.py runserver
```