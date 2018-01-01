#!/bin/bash

# When you add a new package to requirements-to-freeze.txt or update its
# version range you can run this script to update requirements.txt with
# the current version of the package like this:
#
# docker-compose run --rm web ./update-requirements.sh

set -e
if [ -f /.dockerenv ]; then
  pip install -U -r requirements-to-freeze.txt
  pip freeze > requirements.txt
else
  echo "› Update requirements.txt …"
  docker-compose run --rm web ./update-requirements.sh
  echo "› Re-build web container …"
  docker-compose build web
  echo "› Re-start web container …"
  docker-compose restart web
fi
