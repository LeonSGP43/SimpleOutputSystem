# tests/test_api.py
import pytest

from app import app as flask_app


# 初始化测试客户端
@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_output_success(client):
    """测试正常输入场景"""
    response = client.get("/api/output?content=test_input")
    data = response.get_json()
    assert response.status_code == 200
    assert data["code"] == 200
    assert data["data"]["input"] == "test_input"
    assert data["data"]["output"] == "您输入的内容是：test_input"


def test_output_empty_content(client):
    """测试输入为空场景"""
    response = client.get("/api/output?content=")
    data = response.get_json()
    assert response.status_code == 400
    assert data["code"] == 400
    assert data["msg"] == "参数错误：content不能为空"


def test_output_no_content_param(client):
    """测试未传content参数场景"""
    response = client.get("/api/output")
    data = response.get_json()
    assert response.status_code == 400
    assert data["code"] == 400
