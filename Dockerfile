#https://habr.com/ru/post/353234/
#15.11.2019 gunicorn v20.0.0 bug fix https://stackoverflow.com/questions/58786695/how-to-address-oserror-libc-not-found-raised-on-gunicorn-exec-of-flask-app-in
#docker build -t youtube:latest .
#docker run --name youtube-app -d -p 8008:5000 -v /var/apps/dev/proxy-apps/www/youtube-site/app:/home/app --network=mynet --rm youtube_app
#docker run --name youtube-app -p 8008:5000 youtube:latest
#docker run --name youtube-app --network=mynet -d --restart=always youtube:latest
FROM python:3.6-alpine


ENV path /application

WORKDIR ${path}

COPY requirement.txt requirement.txt

RUN python -m venv venv
RUN pip install -r requirement.txt

COPY app app

ENV FLASK_APP main.py
ENV APP_PATH ${path}/app

CMD [". venv/bin/activate && cd app && python main.py"]