#!/bin/bash
set -ex

pip install poetry==1.4.1
poetry install
poetry run poe prepare
