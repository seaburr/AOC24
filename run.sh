#!/usr/bin/env bash

if [ -d day${1} ]; then
  cd day${1}
  python3 main.py
fi
