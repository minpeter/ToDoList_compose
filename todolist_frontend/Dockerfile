FROM nginx:latest
RUN mkdir /todolist
COPY . /todolist
COPY nginx-config/default.conf /etc/nginx/conf.d/default.conf
 
CMD ["nginx", "-g", "daemon off;"]
