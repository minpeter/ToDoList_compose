FROM python:3.9
WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y install sqlite3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

copy . .
RUN chmod +x app.py
EXPOSE 7878
CMD [ "python", "app.py" ]