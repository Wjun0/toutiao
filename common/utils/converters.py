from werkzeug.routing import BaseConverter



class MobileConverter(BaseConverter):
    '''手机号'''
    regex = r'1[3-9]\d{9}'

def register_converters(app):
    '''向flask中添加转换器'''
    app.url_map.converters['mob'] = MobileConverter
