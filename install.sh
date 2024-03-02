#https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04

#!!!install version with pip!!!#
sudo apt update
sudo apt install python3-pip python3-venv -y
sudo apt install python3-dev libpq-dev postgresql postgresql-contrib httping -y

#---install Django
mkdir ~/cy-maxx
cd cy-maxx
python3 -m venv env_cy-maxx
source env_cy-maxx/bin/activate
pip install django psycopg2 django-extensions django-bootstrap-v5 python-whois httpx httpx[cli] googlesearch-python
django-admin startproject app_cymaxx .
python manage.py makemigrations     #for new migrations made
python manage.py migrate
#python manage.py createsuperuser    #[ubuntu/ubuntu] This in in SQLite. Down you rerun the command to create user in PostgreSQL
python manage.py runserver 0.0.0.0:8000     #before run it you must complete with your AWS_Public_IP in Allow_host in settings.py
#---create Django apps
python manage.py startapp recon_passive
python manage.py startapp recon_active

#---configure postgreSQL
#https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-22-04
#sudo -u postgres psql
#   >create database db_cymaxx;
#   >create user cymaxx with password 'cymaxx';
#   >ALTER ROLE cymaxx SET client_encoding TO 'utf8';
#   >ALTER ROLE cymaxx SET default_transaction_isolation TO 'read committed';
#   >ALTER ROLE myproject_user SET timezone TO 'UTC';
#   >GRANT ALL PRIVILEGES ON DATABASE db_cymaxx TO cymaxx;
#-----
sudo ufw allow 8000
#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser

#---install, on PC, pgAdmin for PostgreSQL
#https://www.pgadmin.org/download/
 
#---Install tools---

#golang
sudo snap install go --classic
#subfinder
sudo go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
vi /root/.bashrc
    >export PATH=$PATH:/root/go/bin
sudo mv /root/go/bin/subfinder /usr/local/bin/
vi /home/ubuntu/.config/subfinder/provider-config.yaml
##---configure the provider-config.yaml file with your APIs keys.
##how it works

subfinder -dL targets/../scope.txt -all -oD /recon -json subfinder_recon.json -cs


#### BurpSuite configuration ####
git clone https://github.com/codewatchorg/Burp-UserAgent.git  //for modification of headers into BurpSuite
