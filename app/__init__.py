# app/__init__.py
from app.api import output_bp  # 导入蓝图（确保注册生效）# noqa: F401
from app.extensions import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["DEBUG"])
