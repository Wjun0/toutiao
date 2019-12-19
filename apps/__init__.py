
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import *
import sys

from redis import StrictRedis

#添加common路径到模块查询路径中
from apps.resources.userarticle import article_bp

BASE_DIR= dirname(dirname(abspath(__file__)))
sys.path.insert(0,BASE_DIR +'/common')

from apps.settings.config import config_dict
from utils.contains import EXTRA_ENV_CONFIG

#创建数据库组件
# db = SQLAlchemy() #改到model init中

#创建redis客服端
redis_client = None #type:StrictRedis

def register_extensions(app):
    '''注册组件'''
    from models import db
    #初始化数据库
    db.init_app(app)

    global redis_client
    redis_client = StrictRedis(host=app.config['REDIS_IP'],port=app.config['REDIS_PORT'],decode_responses=True)

def register_blueprint(app):
    from apps.resources.users import user_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)



def create_flask_app(config_type):
    app = Flask(__name__)

    #根据配置类型选择配置子类
    config_class = config_dict[config_type]

    #添加默认配置
    app.config.from_object(config_class)

    #再加载额外配配置
    app.config.from_envvar(EXTRA_ENV_CONFIG,silent=True)

    #返回应用
    return app


def create_app(config_type):
    '''初始化应用'''
    app = create_flask_app(config_type)

    #初始化组件
    register_extensions(app)

    #注册转换器
    from utils.converters import register_converters
    register_converters(app)

    #添加请求钩子
    from utils.middlewares import get_userinfo
    app.before_request(get_userinfo)

    #注册蓝图
    register_blueprint(app)

    return app
