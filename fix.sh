 #!/bin/bash
 
 ./manage.py migrate --fake authors_app zero
 
 cd authors_app/
 find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
 find . -path "*/migrations/*.pyc"  -delete
 cd ../
 
 ./manage.py makemigrations authors_app
 ./manage.py migrate  authors_app --fake-initial

