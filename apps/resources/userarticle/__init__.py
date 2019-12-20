
from flask import Blueprint
from flask_restful import Api

from apps.resources.userarticle.article import ArticleListResource, ArticleDetailResource
from apps.resources.userarticle.follow import FollowResource,DeleteFollowResource
from utils.contains import BASE_URL_PREFIX

article_bp = Blueprint('article',__name__,url_prefix=BASE_URL_PREFIX)

article_api = Api(article_bp)

#添加外层包装
from utils.output_json import output_json
article_api.representation('application/json')(output_json)

#添加类视图
article_api.add_resource(ArticleListResource,'/article')
article_api.add_resource(ArticleDetailResource,'/articles/<int:article_id>')
article_api.add_resource(FollowResource,'/user/followings')
article_api.add_resource(DeleteFollowResource,'/user/followings/<int:target>')
