FROM python:3.9
WORKDIR /todolist_backend

RUN apt-get -y update
RUN apt-get -y install sqlite3

COPY todolist_backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY todolist_backend/. .
RUN chmod +x app.py
EXPOSE 7878
CMD [ "python", "app.py" ]