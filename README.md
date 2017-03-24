- - - - - -

$ cd ../cloudmeb
$ sudo apt-get update
$ sudo apt-get install git
$ sudo apt-get install python-virtualenv
$ sudo apt-get install python3-dev
$ sudo apt-get install gettext
$ sudo apt-get install nginx
$ sudo apt-get install uwsgi
$ virtualenv -p /usr/bin/python3.4 --no-site-packages venv
$ source venv/bin/activate
(venv)$ pip install -r requirements/dev.txt


https://github.com/django-tastypie/django-tastypie/zipball/master

- - - - - -

(venv)$ python manage.py makemessages -l fr --ignore=venv/*
(venv)$ python manage.py makemessages -l en --ignore=venv/*
(venv)$ python manage.py makemessages -l fr -d djangojs --ignore=venv/*
(venv)$ python manage.py makemessages -l en -d djangojs --ignore=venv/*
(venv)$ python manage.py compilemessages

python manage.py makemessages -l fr --ignore=venv/* &&
python manage.py makemessages -l en --ignore=venv/* &&
python manage.py makemessages -l fr -d djangojs --ignore=venv/* &&
python manage.py makemessages -l en -d djangojs --ignore=venv/*

- - - - - -

(venv)$ django-admin startproject cloudmeb
(venv)$ python manage.py startapp mymodule
(venv)$ python manage.py runserver 0.0.0.0:8000

- - - - - -

(venv)$ python manage.py makemigrations benefits categories inputs pages partner_services partners prices products seos services solutions users values websites

- - - - - -

(venv)$ python manage.py dumpdata --format=json --indent=4 > fixtures/initial_data.json

(venv)$ python manage.py dumpdata --format=json --indent=4 benefits > cloudmeb/benefits/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 categories > cloudmeb/categories/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 inputs > cloudmeb/inputs/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 pages > cloudmeb/pages/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 partner_services > cloudmeb/partner_services/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 partners > cloudmeb/partners/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 prices > cloudmeb/prices/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 products > cloudmeb/products/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 seos > cloudmeb/seos/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 services > cloudmeb/services/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 solutions > cloudmeb/solutions/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 users > cloudmeb/users/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 values > cloudmeb/values/fixtures/initial_data.json
(venv)$ python manage.py dumpdata --format=json --indent=4 websites > cloudmeb/websites/fixtures/initial_data.json

- - - - - - 

(venv)$ python manage.py loaddata fixtures/initial_data.json

(venv)$ python manage.py loaddata cloudmeb/websites/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/benefits/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/categories/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/seos/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/pages/fixtures/initial_data.json

(venv)$ python manage.py loaddata cloudmeb/inputs/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/values/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/prices/fixtures/initial_data.json

(venv)$ python manage.py loaddata cloudmeb/solutions/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/services/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/products/fixtures/initial_data.json

(venv)$ python manage.py loaddata cloudmeb/users/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/partners/fixtures/initial_data.json
(venv)$ python manage.py loaddata cloudmeb/partner_services/fixtures/initial_data.json


- - - - - - 

sudo ln -s /home/cloudmeb/cloudmeb/conf/cloudmeb.conf /etc/nginx/sites-enabled/

uwsgi --ini conf/cloudmeb.ini --socket :8001

uwsgi --stop /tmp/cloudmeb.pid

sudo killall -9 uwsgi


# self signed
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /home/cloudmeb/cloudmeb/conf/cloudmeb.key -out /home/cloudmeb/cloudmeb/conf/cloudmeb.crt

# CSR request
sudo openssl req -new -newkey rsa:2048 -nodes -keyout /home/cloudmeb/cloudmeb/conf/cloudmeb.key -out /home/cloudmeb/cloudmeb/conf/cloudmeb.csr