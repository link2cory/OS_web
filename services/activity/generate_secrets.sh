#!/bin/bash

# make secrets directory if it doesn't already exist
mkdir secrets -p

# generate activity-db root password
openssl rand -base64 48 > secrets/db_root_password.txt

# generate activity-db python password
openssl rand -base64 48 > secrets/db_application_password.txt
