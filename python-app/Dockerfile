FROM python:3-alpine

WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

RUN python3 -m pip install --upgrade pip
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install psycopg2
RUN pip install configparser
RUN pip install cherrypy

COPY . .

EXPOSE 8080

CMD [ "python", "PostgreSql.py" ]