#!/bin/bash
# 启动脚本：./run.sh 或 bash run.sh
export FLASK_APP=app
flask run --host=0.0.0.0 --port=${PORT:-5000}

