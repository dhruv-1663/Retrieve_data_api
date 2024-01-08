FROM python:3.9

WORKDIR /task2

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt update

RUN apt install vim -y

COPY ./main .

EXPOSE 5000

# CMD ["flask", "run", "--host=0.0.0.0"]
