from datetime import datetime, timedelta

import random

from flask_restful import Resource
from flask_restful.inputs import regex
from flask_restful.reqparse import RequestParser
from sqlalchemy.orm import load_only

from apps import redis_client
from models import db
from models.user import User
from utils.contains import JWT_DAY_EXPIRE
from utils.parser import mobile as mobile_type

class SMSCodeResource(Resource):
    '''短信验证码'''
    def get(self,mobile):
        code = '%06d'%random.randint(0,999999)

        # redis_client.set('app:code:{}'.format(mobile),code,ex=300)

        print('发送短信：{}'.format(code))

        return {'moblie':mobile}



class LoginResource(Resource):
    '''用户登录'''
    def post(self):
        #获取参数
        parser = RequestParser()
        parser.add_argument('mobile',required=True,location='json',type=mobile_type)
        parser.add_argument('code',required=True,location='json',type=regex(r'\d{6}'))
        args = parser.parse_args()

        mobile = args.mobile
        code = args.code

        key = 'app:code:{}'.format(mobile)
        real_code = redis_client.get(key)
        if not real_code or real_code != code:
            return {'message':'Invalid Code'},400
        #删除验证码
        redis_client.delete(key)

        #校验成功后，查询数据库中的数据
        user = User.query.options(load_only(User.id)).filter_by(mobile=mobile).first()

        if user:#如果有，进行登录，更新登录时间
            user.last_login = datetime.now()
        else:
            #如果没有，进行注册，新增数据
            user = User(mobile=mobile,name=mobile,last_login=datetime.now())
            db.session.add(user)
        db.session.commit()

        #生成jwt
        from utils.jwt_utils import generate_jwt
        token = generate_jwt({'userid':user.id},expiry=datetime.utcnow() + timedelta(days=JWT_DAY_EXPIRE))

        return {'token':token},201


