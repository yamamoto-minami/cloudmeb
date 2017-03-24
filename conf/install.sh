#!/bin/bash

programs=(
	"vim"
	"git"
)

dependencies=(
	"binutils"
	"libproj-dev" 
	"gdal-bin"
	"python-virtualenv"
	"python3-dev"
	"gettext"
	"nginx"
	"uwsgi"
)

function log {
	echo -e "\n$(tput setaf $1)$2$(tput sgr0)\n"
}

function step {
	log "7" "$@"
}

function success {
	log "2" "$@"
}

function error {
	log "1" "$@"
}

function status {
	if [ $@ -eq 0 ]
		then
	    	success "Success"
	else
	    error "Failed"
	fi
}

function chdir {
	step "- Changing working directory"
	cd /home/cloudmeb/cloudmeb
	status $?
}

function update {
	step "- Updating system"
	apt-get --yes update
	status $?
}

function install {
	for package in "$@"
		do 
			step "- Installing $package"
			apt-get --yes install $package
			status $?
	done
}

function venv {
	step "- Creating virtualenv"
	virtualenv -p /usr/bin/python3.4 --no-site-packages venv
	status $?
}

function activate {
	step "- Activating virtualenv"
	source venv/bin/activate
	status $?
}

function requirements {
	step "- Installing requirements"
	pip install -r requirements/dev.txt
	status $?
}

function makemessages {
	step "- Creating i18n po file for domain django and locale fr"
	python manage.py makemessages -l fr --ignore=venv/*
	status $?

	step "- Creating i18n po file for domain django and locale en"
	python manage.py makemessages -l en --ignore=venv/*
	status $?

	step "- Creating i18n po file for domain javascript and locale fr"
	python manage.py makemessages -l fr -d djangojs --ignore=venv/*
	status $?

	step "- Creating i18n po file for domain javascript and locale en"
	python manage.py makemessages -l en -d djangojs --ignore=venv/*
	status $?
}

function compilemessages {
	step "- Compiling po files to mo files"
	python manage.py compilemessages
}


function syncdb {
	step "- Syncronizing database"
	python manage.py syncdb
	status $?
}

function migrate {
	step "- Migrating database schema and data"
	python manage.py migrate
	status $?
}

function collectstatic {
	step "- Collecting static assets"
	python manage.py collectstatic --noinput
	status $?
}

function config {
	step "- Symlinking nginx configuration file"
	ln -s /home/cloudmeb/cloudmeb/conf/cloudmeb.conf /etc/nginx/sites-enabled/
	status $?

	step "- Removing default nginx configuration file"
	rm /etc/nginx/sites-enabled/default
	status $?
}

function start_nginx {
	step "- Starting nginx"
	service nginx reload
	status $?
}

function start_uwsgi {
	step "- Starting uwsgi"
	uwsgi --ini conf/cloudmeb.ini --socket :8001
	status $?
}

# Changing working directory
chdir

# Update system
update

# Install programs
install ${programs[@]}

# Install project dependencies
install ${dependencies[@]}

# Create virtualenv
venv

# Activate virtualenv
activate

# Install requirements 
requirements

# Create po files
makemessages

# Compile po files to mo
compilemessages

# Syncronize database
syncdb

# Migrate database schema and data
migrate

# Collect static assets
collectstatic

# Symlink nginx configuration file
config

# Start nginx
start_nginx

# Start uwsgi
start_uwsgi
