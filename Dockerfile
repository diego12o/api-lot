FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install flask \
pip install flask_httpauth

ENTRYPOINT [ "python3" ]

CMD [ "api.py"]