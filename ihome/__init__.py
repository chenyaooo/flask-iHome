# coding:utf-8

from flask import Flask
from config import config_dict
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import logging
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()

# 构建redis连接对象
redis_store = None

# 设置csrf防范机制 csrf除了校验csrf_token 还用于设置 因此应该是可以被导入的全局变量
csrf = CSRFProtect()  # 延迟加载


# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/logs", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(conf_name):
    """工厂模式创建app"""

    app = Flask(__name__)

    conf = config_dict[conf_name]

    # 绑定配置文件
    app.config.from_object(conf)

    # 初始化数据库
    db.init_app(app)

    global redis_store
    redis_store = redis.StrictRedis(host=conf.REDIS_HOST, port=conf.REDIS_PORT)

    csrf = CSRFProtect(app)  # 延迟加载

    # 将flask中的session存储到redis中
    Session(app)

    # 注册蓝图
    import api_1_0  # 延迟导入

    app.register_blueprint(api_1_0.api, url_prefix="/api/v1_0")

    return app

