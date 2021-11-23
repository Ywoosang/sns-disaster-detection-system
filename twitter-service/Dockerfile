FROM node:alpine
WORKDIR /usr/src
COPY package.json .
COPY package-lock.json .
RUN npm i
COPY main.js .
COPY src/ ./src
RUN npm start
