FROM python:3.8.8
WORKDIR /usr/src
RUN apt-get -y update
RUN apt install wget
RUN apt install unzip  
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN mkdir chrome
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/src/chrome
RUN echo "------------------GOOGLE CHROME VERSION -----------------------------"
RUN google-chrome --version
RUN echo "---------------------------------------------------------------------"
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
CMD [ "python", "app/main.py" ]