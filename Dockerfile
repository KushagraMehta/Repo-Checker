FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

# RUN adduser -D server
# USER server

CMD [ "python", "./code/manager.py", "runserver", "0.0.0.0:8000" ]