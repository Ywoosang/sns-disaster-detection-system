FROM python:3

WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN apt-get install -yqq unzip curl
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/app/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY crawl.py .
CMD [ "python", "./crawl" ]