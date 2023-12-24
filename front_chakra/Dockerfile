# Stage 1: Build the frontend
FROM node:18 
WORKDIR /app

COPY ./frontend /app/

RUN npm install
RUN npm run build
RUN npm install -g http-server

CMD ["http-server", "./dist", "-p", "8000"]
