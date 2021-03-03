FROM python:3.8.6-buster

COPY StarWars /StarWars
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY final_model.h5 /final_model.h5

CMD uvicorn StarWars.api.simple:app --host 0.0.0.0 --port $PORT
