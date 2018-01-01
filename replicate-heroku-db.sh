#!/bin/bash

set -e

echo "This will capture a database backup on Heroku, download it to your
computer and populate your local database with it."

while true; do
    read -p "Do you want to capture a new database snapshot on Heroku (y) or use the latest one (n)? " yn
    case $yn in
        [Yy]* ) echo "Capturing database backup on Heroku …" ; heroku pg:backups capture -a pb-{{ project_name }}; break;;
        [Nn]* ) echo "Using the latest database snapshot." ; break;;
        * ) echo "Please answer y or n.";;
    esac
done

echo "Downloading backup from Heroku …"
FILENAME=latest-`date -u +"%Y-%m-%dT%H:%M:%SZ"`.dump
curl -o $FILENAME `heroku pg:backups public-url -a {{ project_name }}`

echo "Restoring backup to local Postgres database …"
docker run --rm -it --link {{ project_name }}_db_1:postgres \
    --net {{ project_name }}_default --volume $PWD/:/tmp/ postgres pg_restore \
    --clean -h postgres -U postgres -d postgres --no-acl --no-owner \
    /tmp/$FILENAME || \
    (echo "Unable to import backup into local Postgres database." && exit 1)

echo "Deleting downloaded backup file …"
rm $FILENAME

echo "Done."
