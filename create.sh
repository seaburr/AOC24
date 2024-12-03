#!/usr/bin/env bash

if [ ! -d day${1} ]; then
  mkdir day${1}
  cd day${1}
  touch main.py
  touch test.txt
  touch input.txt
  touch README.md
fi
