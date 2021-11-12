FROM node:alpine
WORKDIR /usr/src
COPY package.json .
COPY package-lock.json .
COPY tsconfig.json .
COPY src/ ./src
RUN npm i
RUN npm run build
