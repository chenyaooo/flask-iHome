# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha


# url: /api/v1_0/image_codes/<image_code_id>
# method: get
# 传入参数
# 返回值


@api.route("/api/v1_0/image_codes/<image_code_id>")
def verify_code(image_code_id):
    """提供图片验证码"""
    captcha.generate_captcha()