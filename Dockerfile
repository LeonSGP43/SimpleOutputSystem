# 基础镜像（选择Python 3.9 slim版本，体积小）
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖（避免后续安装Python依赖报错）
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖清单
COPY requirements.txt .

# 安装Python依赖（--no-cache-dir减少镜像体积）
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码（.dockerignore中已忽略不需要的文件）
COPY . .

# 创建日志目录（避免权限问题）
RUN mkdir -p /app/logs && chmod 777 /app/logs

# 暴露端口（与配置文件一致）
EXPOSE 51000

# 启动命令（生产环境用gunicorn替代Flask内置服务器，性能更好）
CMD ["gunicorn", "--bind", "0.0.0.0:51000", "-w", "4", "app:app"]
