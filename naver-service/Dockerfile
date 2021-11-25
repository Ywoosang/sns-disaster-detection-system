FROM node:alpine
WORKDIR /usr/src
COPY package.json .
COPY package-lock.json .
RUN npm i
RUN npm install pm2 -g
COPY src ./src
