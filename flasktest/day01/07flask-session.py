from flask_session import Session
from redis import StrictRedis
from flask import Flask, session
# from flask_session import Session

app = Flask(__name__)


app.config['SESSION_TYPE'] ='redis'  #设置存储系统
app.config['SESSION_REDIS'] = StrictRedis(host='192.168.59.128',port=6379)
app.config['SESSION_USE_SIGNER'] = True
app.config['SECRET_KEY'] =  'test'  #设置应用的密钥

#初始化组件
Session(app)

@app.route('/index')
def home():
    session['userid'] = 11
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)

