from flask import g, request
from flask_restful import Resource
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.orm import load_only

from models import db
from models.article import Channel, UserChannel
from utils.decorators import login_required


class UserChannelResource(Resource):
    '''获取用户频道'''
    method_decorators = {'put':[login_required]}
    def get(self):
        userid = g.userid
        if userid:
            # user_channel = db.session.query(Channel.id,Channel.name).\
            #     join(UserChannel,Channel.id==UserChannel.channel_id).\
            #     filter(UserChannel.user_id==userid).all()
            user_channel = Channel.query.options(load_only(Channel.id,Channel.name)).\
                join(UserChannel,UserChannel.channel_id ==Channel.id).\
                filter(UserChannel.user_id ==userid,UserChannel.is_deleted==False).\
                order_by(UserChannel.sequence).all()

            if len(user_channel) ==0:#如果你没有，就用默认的推荐
                user_channel = Channel.query.options(load_only(Channel.id, Channel.name)). \
                    filter(Channel.is_default == True).all()

        else:
            user_channel =  Channel.query. options(load_only(Channel.id,Channel.name)).\
                filter(Channel.is_default == True).all()

        channels = [channel.to_dict() for channel in user_channel]

        #插入推荐频道
        channels.insert(0,{'id':0,'name':'推荐'})

        return {'channels':channels}


    def put(self):
        '''修改用户频道'''
        channels = request.json.get('channels')

        #将数据库中的数据全部逻辑删除
        UserChannel.query.filter(UserChannel.is_deleted ==False,UserChannel.user_id ==g.userid).\
            update({'is_deleted':True})

        #更新数据
        for channel in channels:
            statement = insert(UserChannel).values(user_id=g.userid,channel_id=channel['id'],sequence=channel['seq']).\
                on_duplicate_key_update(sequence=channel['seq'],is_deleted=False)
            db.session.execute(statement)
        db.session.commit()

        return {'channels':channels}



class AllChannelsResource(Resource):
    '''获取所有的频道'''
    def get(self):
        channels = Channel.query.options(load_only(Channel.id,Channel.name)).all()
        channels = [channel.to_dict() for channel in channels]

        return {'channels':channels}



