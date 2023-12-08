FROM node:18-alpine

WORKDIR /webapp

COPY ./package.json /webapp/

RUN npm install

COPY . .

CMD npm run dev

EXPOSE 8000
