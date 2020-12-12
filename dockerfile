FROM python:3.7.6

WORKDIR /user/source/net

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python","app.py","index.html","parents.html","meeting.html" ]
