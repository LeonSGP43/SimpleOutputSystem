#!/usr/bin/env python
"""项目根目录启动脚本：python main.py"""
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["DEBUG"])
    print("Hello World")
    print(app.config)
    print(app.config["PORT"])
    print(app.config["DEBUG"])
