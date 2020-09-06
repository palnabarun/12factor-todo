#! /usr/bin/env bash

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}

uvicorn asgi:api --host $HOST --port $PORT $@
