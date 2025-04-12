pip intall -r requirements.txt
cd local-democracy
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
