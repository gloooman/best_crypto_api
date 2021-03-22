FROM python:3.9
RUN apt-get update
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
COPY . /app
RUN pip install flask-cors --upgrade
RUN pip install -r requirements.txt


#CMD gunicorn -w 13 -b 0.0.0.0:5000 main:app
CMD ["python", "main.py"]

