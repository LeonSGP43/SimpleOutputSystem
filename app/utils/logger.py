# app/utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler

from pythonjsonlogger import jsonlogger

from app.config import get_config

config = get_config()


def setup_logger() -> logging.Logger:
    """初始化日志系统"""
    logger = logging.getLogger("output-service")
    logger.setLevel(config.LOG_LEVEL)
    logger.propagate = False  # 避免重复打印

    # 创建日志目录
    log_dir = "./logs"
    os.makedirs(log_dir, exist_ok=True)

    # JSON格式日志（结构化，方便检索）
    log_format = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(module)s %(message)s %(extra)s"
    )

    # 控制台输出（开发环境）
    if config.DEBUG:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)

    # 文件输出（按大小轮转，生产环境）
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, "app.log"),
        maxBytes=10 * 1024 * 1024,  # 单个文件10MB
        backupCount=3,  # 保留3个备份
        encoding="utf-8",
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger


# 全局logger实例（所有模块直接导入使用）
logger = setup_logger()
