FROM python:3.7
MAINTAINER Ivan Leonov "kepolol@gmail.com"
RUN apt-get install -y libsm6 libxext6 libxrender-dev
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "run.py"]
