#!/bin/bash
set -ex

curl -LsSf https://astral.sh/uv/install.sh | sh
uv run poe prepare
