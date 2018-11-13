FROM python:2.7
WORKDIR /srv
RUN pip install requests
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ /srv/
