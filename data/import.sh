#!/bin/bash -eu

redis-cli -h redis --pipe < db.rdb 2>&1

trap 'echo "SIGINT" && exit 0' SIGINT
while true; do
  sleep 1
done
