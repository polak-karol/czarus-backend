FROM python:3.11.2-alpine3.16

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk add build-base
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /usr/src/app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]