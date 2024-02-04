#https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04

#!!!install version with pip!!!#
sudo apt update
sudo apt install python3-pip python3-venv -y
#-----
mkdir ~/cy-maxx
cd cy-maxx
python3 -m venv env_cy-maxx
source env_cy-maxx/bin/activate
pip install django
#-----
django-admin startproject app_cymaxx .
python manage.py makemigrations     #for new migrations made
python manage.py migrate
python manage.py createsuperuser    #ubuntu/ubuntu
python manage.py runserver 0.0.0.0:8000     #before run it you must complete with your AWS_Public_IP in Allow_host in settings.py