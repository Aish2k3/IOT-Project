FROM node:alpine

WORKDIR /iotweb

COPY ./package.json /iotweb

RUN npm install

COPY . .

CMD npm start
