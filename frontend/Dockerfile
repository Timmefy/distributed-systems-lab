# Stage 1: Build the Angular app in Node.js
FROM node:20.12.2
WORKDIR /app
COPY todo-lab/package.json .
COPY ./todo-lab .
RUN npm install -g @angular/cli
RUN npm install

EXPOSE 4200
CMD ["ng", "serve", "--host", "0.0.0.0"]