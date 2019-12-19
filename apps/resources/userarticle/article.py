from flask import request, g
from flask_restful import Resource
from flask_restful.inputs import natural, positive
from flask_restful.reqparse import RequestParser
from sqlalchemy.orm import load_only

from models import db
from models.article import Article, ArticleContent, Attitude, Collection
from models.user import User, Relation
from utils.contains import PER_PAGE_COUNT


class ArticleListResource(Resource):
    '''文章列表'''
    def get(self):
        parser = RequestParser()
        parser.add_argument('channel_id',required=True,location='args',type=natural)
        parser.add_argument('page',required=True,location='args',type=positive)

        args = parser.parse_args()
        channel_id = args.channel_id
        page = args.page

        if channel_id == 0:
            return {'pre_page':0,'results':[]}

        #查询文章
        pn = db.session.query(Article.id,Article.title,Article.user_id,Article.ctime,User.name,
                              Article.comment_count).\
            join(User,Article.user_id ==User.id).\
            filter(Article.channel_id ==channel_id,Article.status ==Article.STATUS.APPROVED).\
            order_by(Article.id.desc()).\
            paginate(page,PER_PAGE_COUNT)

        articles = [{
            'art_id':article.id,
            'title':article.title,
            'pubdate':article.ctime.isoformat(),
            'aut_name':article.name,
            'comm_count':article.comment_count
        }for article in pn.items]

        return {'pre_page':pn.page + 1,'results':articles}



class ArticleDetailResource(Resource):
    '''文章详情'''
    def get(self,article_id):

        data = db.session.query(Article.id,Article.title,Article.ctime,Article.user_id,User.name,User.profile_photo,ArticleContent.content).\
            join(User,Article.user_id ==User.id).\
            join(ArticleContent,ArticleContent.id ==Article.id).\
            filter(Article.id ==article_id).first()

        article_dict = {
            'art_id':data.id,
            'title':data.title,
            'pubdate':data.ctime.isoformat(),
            'aut_photo':data.profile_photo,
            'aut_name':data.name,
            'content':data.content
        }
        userid = g.userid
        attribute_dict = {'is_followed':False,'attitude':-1,'is_collected':False}

        if userid:#如果用户登录
            relation = db.session.query(Relation.id).\
                filter(Relation.user_id==g.userid,Relation.target_user_id==data.user_id,Relation.relation==Relation.RELATION.FOLLOW).first()
            attribute_dict['is_followed'] = True if relation else False

            attitude = db.session.query(Attitude.attitude).filter(Attitude.user_id==g.userid,Attitude.article_id==data.id).first()
            attribute_dict['is_collected'] = attitude[0] if attitude else -1

            collection = db.session.query(Collection.id).filter(Collection.user_id==userid,Collection.article_id==data.id,Collection.is_deleted==False).first()
            attribute_dict['is_collected'] =True if collection else False
        article_dict.update(attribute_dict)

        return article_dict


