FROM nginx:latest
RUN mkdir /todolist_frontend
COPY todolist_frontend/. /todolist_frontend
COPY todolist_frontend/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
