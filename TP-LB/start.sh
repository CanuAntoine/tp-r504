#!/bin/bash

docker network create tp1b > /dev/null 2>&1 

docker build -t im-nginx-lb -f tp-A/Dockerfile .

mkdir -p shared1 shared2

echo "<h1>Hello 1" > shared1/index.html
echo "<h1>Hello 2" > shared2/index.html

docker run -d \
    --name nginx1 \
    -p 8081:80 \
    -v $PWD/shared1:/usr/share/nginx/html \
    --rm \
    im-nginx-lb 

docker run -d \
    --name nginx2 \
    -p 8082:80 \
    -v $PWD/shared2:/usr/share/nginx/html \
    --rm \
    im-nginx-lb 