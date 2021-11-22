FROM node:alpine
WORKDIR /usr/src
COPY package.json .
COPY package-lock.json .
COPY main.js .
COPY src/ ./src
COPY controller/ ./controller
COPY model/ ./model
RUN npm i
RUN npm start