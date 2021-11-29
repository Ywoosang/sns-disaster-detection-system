FROM python:3.8.8
WORKDIR /usr/src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY cc.ko.300.bin .
# RUN gunzip cc.ko.300.bin.gz
RUN pip install regex
RUN pip install -U flask-cors
COPY app.py .
COPY util.py .
COPY model.py .
COPY fword_list.txt .