set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
if [[ $CREATE_SUPERUSER]];
then
    python manage.py createsuperuser --username admin --email 123@example.com
fi
