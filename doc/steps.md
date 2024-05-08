👉 [Back to main Document](./index.md)
#### Main Steps
`django-admin startproject <project-name> <location>`
- In this project: <project-name> is core.

`python manage.py startapp <app-name>`
- In this project: <app-name> is store.

##### To run this project
```
python manage.py runserver
    or:
python manage.py runserver <customize-port>
```
#### To migrate Database
```
python manage.py makemigrations
python manage.py migrate
```