#!/usr/bin/env sh

echo "Bring up the containers"
docker-compose up -d

echo "Bring up the measurer"
python3 measurer.py
