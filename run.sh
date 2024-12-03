#!/usr/bin/env bash

if [ -d day${1} ]; then
  cd day${1}
  time python3 main.py
fi
