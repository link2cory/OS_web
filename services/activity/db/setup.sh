#!/bin/sh

PYTHON_DB_PASSWORD=$(cat $PYTHON_DB_PASSWORD_FILE)

mongo admin --eval "db.createUser({user: 'python', pwd: '$PYTHON_DB_PASSWORD', roles:[{role:'readWrite', db:'optimized_self'}]});"
# mongo admin --eval "db.createUser({user: 'user_admin', pwd: 'user_admin_password', roles:[{role:'userAdmin', db:'admin'}]});"
