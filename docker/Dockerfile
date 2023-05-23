FROM python:3.7-slim

#RUN apt-get update && apt-get install -y blender

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
