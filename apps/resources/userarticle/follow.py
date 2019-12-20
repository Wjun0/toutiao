from flask import request, g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask_restful.inputs import positive
from sqlalchemy.orm import load_only

from models import db
from models.user import Relation, User


class FollowResource(Resource):
    '''用户关注'''
    def post(self):
        userid = g.userid
        parser = RequestParser()
        parser.add_argument('target',required=True,location='json',type=positive)
        args = parser.parse_args()
        target_id = args.target

        if userid ==target_id:
            return {'message':"can not follow self"},400

        #先查询关系是否存在
        relation = Relation.query.options(load_only(Relation.id)).\
            filter(Relation.user_id ==userid,Relation.target_user_id==target_id).first()

        if relation:#更新关系为关注
            relation.relation = Relation.RELATION.FOLLOW

        else:#不存在关系，添加关系
            relation = Relation(user_id = userid,target_user_id=target_id,relation=Relation.RELATION.FOLLOW)
            db.session.add(relation)
        db.session.commit()

        return {'target':target_id},201


    def get(self):
        userid = g.userid
        parser = RequestParser()
        parser.add_argument('page',location='args',type=positive)
        parser.add_argument('per_page',location='args',type=positive)
        args = parser.parse_args()

        page = args.page
        per_page = args.per_page

        pn = User.query.options(load_only(User.id,User.name,User.profile_photo,User.fans_count)).\
            join(Relation,User.id==Relation.user_id).\
            filter(Relation.relation==Relation.RELATION.FOLLOW,Relation.user_id ==userid).\
            order_by(Relation.id.desc()).paginate(page,per_page)


        fans = Relation.query.options(load_only(Relation.user_id)).\
            filter(Relation.target_user_id ==userid,Relation.relation==Relation.RELATION.FOLLOW).all()

        results = []
        for author in pn.items:
            user_dict = {
                'id':author.id,
                'name':author.name,
                'photo':author.profile_photo,
                'fans_count':author.fans_count,
                'mutual_follow':False
            }

            for fan in fans:
                if author.id ==fan.user_id:
                    user_dict['mutual_fallow'] = True
                    break
            results.append(user_dict)

        return {'tatal_count':pn.total,'page':pn.page,'per_page':per_page,'results':results}



class DeleteFollowResource(Resource):
    '''取消关注'''
    def delete(self,target):
        userid = g.userid
        Relation.query.options(load_only(Relation.id)).\
            filter(Relation.user_id==userid,Relation.target_user_id==target).\
            update({'relation':Relation.RELATION.DELETE})
        db.session.commit()

        return {'message':'ok'}









