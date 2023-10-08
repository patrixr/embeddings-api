#!/bin/sh

docker run --rm -it \
  -w "/root" -p 8000:8000 \
  -v `pwd`:/root python:3.11 bash \
  -c "pip install -r requirements.txt && uvicorn instructor_api.api:app --host 0.0.0.0 --port 8000"