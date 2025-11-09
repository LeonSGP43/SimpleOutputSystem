# app/api/__init__.py
from flask import Blueprint, jsonify, request

# 加载配置
from app.config import get_config
from app.extensions import app
from app.utils.logger import logger

# 创建接口蓝图（拆分接口，大厂常用）
output_bp = Blueprint("output", __name__, url_prefix="/api")


@output_bp.get("/output")
def get_output():
    """
    核心接口：接收用户输入的content参数，返回格式化输出
    请求示例：GET /api/output?content=hello_world
    响应示例：{"code":200,"data":{"input":"hello_world","output":"您输入的内容是：hello_world"}}
    """
    # 1. 获取并校验参数
    content = request.args.get("content", "").strip()
    if not content:
        logger.warning("用户输入为空", extra={"input": content})
        return jsonify({"code": 400, "msg": "参数错误：content不能为空"}), 400

    # 2. 业务逻辑（极简：格式化输出）
    formatted_output = f"您输入的内容是：{content}"
    logger.info(
        "输出接口调用成功", extra={"input": content, "output": formatted_output}
    )

    # 3. 返回响应
    return jsonify(
        {"code": 200, "data": {"input": content, "output": formatted_output}}
    )


# 注册蓝图到Flask应用
app.register_blueprint(output_bp)


app.config.from_object(get_config())
