#!/bin/bash
# Prepare log files and start outputting logs to stdout
# mkdir -p /usr/local/var/log/uwsgi

touch portfolio.log
chmod 644 portfolio.log
chown www-data portfolio.log
chown www-data db.sqlite3
chown www-data /webapp

chown www-data media

# Webapp commands
python3 manage.py makemigrations
python3 manage.py migrate                  # Apply database migrations
python3 manage.py loaddata fixtures/latest.json
python3 manage.py collectstatic --noinput  # Collect static files
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
