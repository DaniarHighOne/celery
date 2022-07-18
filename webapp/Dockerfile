FROM python:3.9
# RUN apt-get update -y
# RUN apt-get updgrade -y

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./src ./src
CMD ["python3", "./src/manage.py", "runserver", "0.0.0.0:8000" ]