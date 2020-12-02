FROM python:3.9

RUN apt-get -y update
RUN apt-get install -y chromium chromium-driver

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

EXPOSE 5000

CMD [ "python", "./server.py" ]