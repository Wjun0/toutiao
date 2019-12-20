from flask import Blueprint
from flask_restful import Api

from apps.resources.comments.releasecomment import CommentResource
from utils.contains import BASE_URL_PREFIX

comment_bp = Blueprint('comment',__name__,url_prefix=BASE_URL_PREFIX)

comment_api = Api(comment_bp)

#添加外层包装
from utils.output_json import output_json
comment_api.representation('application/json')(output_json)


comment_api.add_resource(CommentResource,'/comments')

