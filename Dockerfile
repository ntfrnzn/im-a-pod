FROM python:alpine3.7

RUN pip install flask==0.12.2 kubernetes==3.0.0 gunicorn
COPY im-a-pod.py .

CMD gunicorn -b 0.0.0.0:5000 im-a-pod:app

