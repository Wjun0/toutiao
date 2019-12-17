
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'

app.url_map.converters['mob'] = MobileConverter

@app.route('/demo/<mob:mobile>')
def home(mobile):
    print(mobile)
    return 'home'


@app.route('/index/<int:userid>')  #int 为内置转换器
def index(userid):
    print(userid)
    return 'hello flask'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)


