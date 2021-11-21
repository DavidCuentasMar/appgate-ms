FROM nickgryg/alpine-pandas:latest
WORKDIR /app
COPY . /app
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip3 install -r requirements.txt