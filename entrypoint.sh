#!/usr/bin/env bash
nohub python cronjob.py &

uwsgi --chdir=/code \
      --module=main \
      --callable=app \
      --master \
      --http-socket=0.0.0.0:8000 \
      --processes=1 \
      --harakiri=30 \
      --max-requests=5000
