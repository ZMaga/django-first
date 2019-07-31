FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /authors_site
WORKDIR /authors_site
COPY requirements.txt /authors_site
RUN pip install -r requirements.txt
COPY . /authors_site
