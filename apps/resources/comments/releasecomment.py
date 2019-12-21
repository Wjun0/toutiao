from flask import g, request
from flask_restful import Resource
from flask_restful.inputs import positive
from flask_restful.reqparse import RequestParser
from sqlalchemy.orm import load_only

from models import db
from models.article import Comment, Article
from models.user import User


class CommentResource(Resource):
    '''发布评论'''
    def post(self):
        target = request.json.get('target')
        print(target)
        userid = g.userid
        parser = RequestParser()
        parser.add_argument('target',required=True,location='json',type=positive)
        parser.add_argument('content',required=True,location='json')

        parser.add_argument('parent_id',location='json',type=positive)
        args = parser.parse_args()

        target = args.target
        content = args.content
        parent_id = args.parent_id

        if not len(content):
            return {'message':'content can not null'}
        if parent_id:#如果有，说明是回复
            #生成回复
            comment = Comment(article_id= target,user_id=userid,parent_id=parent_id,content=content,)

            #回复加一
            Comment.query.options(load_only(Comment.id)).\
                filter(Comment.id ==parent_id).update({'reply_count':Comment.reply_count +1})
        else:

            comment = Comment(user_id=userid,article_id=target,content=content)

            #评论数加一
            Article.query.options(load_only(Article.id)).filter(Article.id==target).\
                update({"comment_count":Article.comment_count + 1})

        db.session.add(comment)
        db.session.commit()

        #返回结果
        return {'com_id':comment.id,'target':target}

    def get(self):
        '''获取评论列表'''
        parser = RequestParser()
        parser.add_argument('source', required=True, location='args', type=positive)
        parser.add_argument('offset', location='args',default=0)
        parser.add_argument('limit',location='args',default=20)

        args = parser.parse_args()
        source = args.source
        offset = args.offset
        limit = args.limit

        comments = db.session.query(Comment.id, Comment.user_id, User.name, User.profile_photo,Comment.ctime,Comment.content,
                         Comment.reply_count,Comment.like_count).\
            join(User,User.id ==Comment.user_id).\
            filter(Comment.article_id ==source,Comment.id>offset).\
            limit(limit).all()

        results = [{
            'com_id':comment.id,
            'aut_id':comment.user_id,
            'aut_name':comment.name,
            'aut_photo':comment.profile_photo,
            'pubdate':comment.ctime.isoformat(),
            'content':comment.content,
            'reply_count':comment.reply_count,
            'like_count':comment.like_count
        }for comment in comments]

        #查询评论总数
        count = Comment.query.filter(Comment.article_id == source,Comment.parent_id==0).count()

        #获取最后一条评论
        last_comment = Comment.query.options(load_only(Comment.id)).filter(Comment.article_id==source,Comment.parent_id==0).\
            order_by(Comment.id.desc()).limit(1).first()

        #获取本次请求的最后一条评论的id
        last_id =results[-1]['com_id'] if len(results) else None

        end_id = last_comment.id if count else  None

        return {'total_count':count,'end_id':end_id,'last_id':last_id,'results':results}










