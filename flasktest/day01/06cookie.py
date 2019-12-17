
from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/index')
def home():
    # 创建响应对象
    response = make_response('index')

    #设置响应头
    response.set_cookie('per_page','10',max_age=3600)

    #删除cookie数据 本质 max-age=0
    # response.delete_cookie('per_page')

    return response

@app.route('/demo')
def demo():
    #获取cookie
    par_page = request.cookies.get('per_page')
    return par_page


if __name__ == '__main__':
    app.run(debug=True)