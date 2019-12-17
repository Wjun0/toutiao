
from flask import Flask

app = Flask(__name__)

# def  prepare():
#     print('before_request:一般用于请求的准备工作，参数解析，数据统计，黑名单过滤')
#
# apps.before_request(prepare)


#另一种用法
@app.before_request
def  prepare():
    print('before_request:一般用于请求的准备工作，参数解析，数据统计，黑名单过滤')


@app.route('/')
def index():
    return 'index'



if __name__ == '__main__':
    app.run(debug=True)


