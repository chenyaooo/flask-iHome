# coding:utf-8

from flask import request
from . import api


# POST /api/v1_0/users
@api.route("/users", methods=["POST"])
def register():
    """用户注册"""
    # 接受参数 手机号 短信验证码 密码  前端以json格式传来数据
    # data 接受所有的原始数据
    # request.data

    req_dict = request.get_json()  # get_json能将请求体中的json转变为字典

    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    pwd = req_dict.get("pwd")

    # 校验数据
    if not all([mobile, sms_code, pwd]):
        res = {
            # "errno": RET.
        }
    # 业务逻辑
    # 获取短信验证码
    # 判断短信验证码是否过期
    # 判断手机号是否被注册
    # 保存用户数据到数据库中
    # 记录用户的登陆状态
    # 返回响应


def login():
    """登陆"""
    pass