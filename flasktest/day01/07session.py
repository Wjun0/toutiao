from datetime import timedelta

from flask import Flask, session

app = Flask(__name__)

#设置应用的密钥 用于对session数据精选签名
app.secret_key = 'test'

#设置session的过期时间,默认为30天
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/index')
def home():
    #记录session数据 类字典对象
    session['userid'] =11

    #设置session支持过期时间
    session.permanent = True
    return 'index'



@app.route('/demo')
def demo():
    #获取session
    print(session.get('userid'))

    #删除session
    session.pop('userid',None)
    return 'demo'


if __name__ == '__main__':
    app.run(debug=True)