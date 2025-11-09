# app/config/__init__.py
import os

from dotenv import load_dotenv

# 加载.env文件
load_dotenv()


class Config:
    """基础配置"""

    SECRET_KEY = os.getenv("SECRET_KEY")
    PORT = int(os.getenv("PORT", 5000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


class DevelopmentConfig(Config):
    """开发环境配置"""

    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置"""

    DEBUG = False


# 配置映射（根据环境变量切换）
config_map = {"development": DevelopmentConfig, "production": ProductionConfig}


def get_config():
    """获取当前环境的配置"""
    env = os.getenv("FLASK_ENV", "production")
    return config_map[env]
