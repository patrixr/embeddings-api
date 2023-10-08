#!/bin/sh

docker run --rm -it -w "/root" -p 8000:8000 -v `pwd`:/root --entrypoint bash python:3.11  