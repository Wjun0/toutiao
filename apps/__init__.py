
from flask import Flask
from os.path import *
import sys

#添加common路径到模块查询路径中
BASE_DIR= dirname(dirname(abs(__file__)))
sys.path.insert(0,BASE_DIR +'/common')

from apps.settings.config import config_dict
from utils.contains import EXTRA_ENV_CONFIG

def create_app(config_type):
    app = Flask(__name__)

    #根据配置类型选择配置子类
    config_class = config_dict[config_type]

    #添加默认配置
    app.config.from_object(config_class)

    #再加载额外配配置
    app.config.from_envvar(EXTRA_ENV_CONFIG,silent=True)

    #返回应用
    return app

