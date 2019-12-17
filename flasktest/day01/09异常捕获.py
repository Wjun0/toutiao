from flask import Flask, abort

app = Flask(__name__)

#捕获http错误
@app.errorhandler(404)
def error_404(e): #一旦捕获异常，必须定义形参来接受具体的错误
    return '访问的页面不存在————%s'%e

#还可以捕获系统内置的错误
@app.errorhandler(ZeroDivisionError)
def error_zero(e):
    return e


#捕获http错误
@app.errorhandler(401)
def error_404(e):
    return '401————%s'%e


@app.route('/')
def index():
    # a = 1/0
    #只能主动抛出http错误
    abort(401)
    return 'index'



if __name__ == '__main__':
    app.run(debug=True)
