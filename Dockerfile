FROM node:latest
LABEL dev="trader-heidis"

WORKDIR /usr/app/

COPY . .

CMD [ "/bin/bash" ]