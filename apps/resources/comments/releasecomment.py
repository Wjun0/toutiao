from flask import g
from flask_restful import Resource
from flask_restful.inputs import positive
from flask_restful.reqparse import RequestParser
from sqlalchemy.orm import load_only

from models import db
from models.article import Comment, Article



class CommentResource(Resource):
    '''发布评论'''
    def post(self):
        userid = g.userid
        parser = RequestParser()
        parser.add_argument('target',required=True,location='json',type=positive)
        parser.add_argument('content',required=True,location='json')
        args = parser.parse_args()

        target = args.target
        content = args.content

        comment = Comment(user_id=userid,article_id=target,content=content)
        db.session.add(comment)

        #评论数加一
        Article.query.options(load_only(Article.id)).filter(Article.id==target).\
            update({"comment_count":Article.comment_count + 1})
        db.session.commit()

        #返回结果
        return {'com_id':comment.id,'target':target}






