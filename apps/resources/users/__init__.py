from flask import Blueprint

from flask_restful import Api
from apps.resources.users.passport import SMSCodeResource, LoginResource

user_bp = Blueprint('user',__name__,url_prefix='/app/v1_0')

#创建蓝图对象
user_api = Api(user_bp)

#添加外层包装
from utils.output_json import output_json
user_api.representation('application/json')(output_json)

#添加类试图
user_api.add_resource(SMSCodeResource,'/sms/codes/<mob:mobile>')
user_api.add_resource(LoginResource,'/authorizations')




