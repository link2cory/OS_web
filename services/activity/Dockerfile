# base image
FROM python:3.7.2-alpine

ARG env

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add app
COPY ./manage.py /usr/src/app/manage.py
COPY ./project /usr/src/app/project
COPY ./tests /usr/src/app/tests

# add and install requirements
COPY ./requirements-${env}.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add the appropriate entrypoint script
COPY ./entrypoint-${env}.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# run server
CMD ["/usr/src/app/entrypoint.sh"] 
#CMD python manage.py run -h 0.0.0.0
