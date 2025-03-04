set -o errexit

pip3 install django
pip3 install requests
pip3 install psycopg2
pip3 install beautifulsoup4

pip3 install -r requirements.txt

python3 manage.py migrate
python3 manage.py collectstatic --noinput