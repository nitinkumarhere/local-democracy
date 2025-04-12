
## local-democracy
# create virtualenv
virtualenv env

# activate env
source env/bin/activate

# install requirements
pip intall -r requirements.txt

# change directory to repository
cd local-democracy

# make migrations
python manage.py makemigrations

# migrate
python manage.py migrate

# runserver
python manage.py runserver 
