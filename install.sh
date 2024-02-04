#https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04

#!!!install version with pip!!!#
sudo apt update
sudo apt install python3-pip python3-venv

mkdir cy-maxx
cd cy-maxx
python3 -m venv env_cy-maxx
source env_cy-maxx/bin/activate
pip install django