FROM python:3.13-slim-bookworm@sha256:3531ec44ed35e581f573519aaa2b0f3ea74045327f40d653551ecedadb2db57d

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
