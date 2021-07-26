## ==== 데이터베이스초기화을 진행할 경우 =====
1. >  todo.db 삭제
2. >  dbInit.py 실행 

## ==== 도커를 이용하는 경우 ====
1. > docker build -t todolistbackend .
2. >  docker run -d --rm --name todolistBackend -p 7878:7878 todolistbackend