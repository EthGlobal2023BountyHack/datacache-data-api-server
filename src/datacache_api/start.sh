source env.sh
nohup /var/www/server/datacache-data-api-server/venv/bin/python manage.py runserver >> runlog.txt 2>&1 &
